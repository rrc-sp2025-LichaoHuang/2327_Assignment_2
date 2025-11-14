__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging
# *******************************************************************************
# NEW IMPORT
from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.saving_account import SavingAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date
from bank_account.bank_account import BankAccount

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************






def load_data() -> tuple[dict, dict]:
    """
    Load client and bank account data from the CSV files in the data directory.

    Returns:
        tuple(dict, dict):
            - client_listing: {client_number: Client}
            - accounts: {account_number: BankAccount}
    """

    # Two dictionaries required by assignment spec
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA
    try:
        with open(clients_csv_path, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    # Convert CSV values into proper data types for Client constructor
                    client_number = int(row["client_number"])
                    first = row["first_name"]
                    last = row["last_name"]
                    email = row["email_address"]

                    # Create Client object
                    client_obj = Client(client_number, first, last, email)

                    # Store in dictionary using client_number as the key
                    client_listing[client_number] = client_obj

                except Exception as e:
                    # Any client creation error is logged but processing continues
                    logging.error(f"Unable to create client: {e}")

    except Exception as e:
        logging.error(f"Error reading clients.csv: {e}")

    # READ ACCOUNT DATA
    try:
        with open(accounts_csv_path, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    # Convert CSV fields into strongly-typed values
                    acc_num = int(row["account_number"])
                    client_num = int(row["client_number"])
                    balance = float(row["balance"])
                    date_created = date.fromisoformat(row["date_created"])
                    acc_type = row["account_type"]

                    # Helper to convert "Null" to actual str None
                    def to_float(value):
                        return float(value) if value != "Null" else None

                    overdraft_limit = to_float(row["overdraft_limit"])
                    overdraft_rate = to_float(row["overdraft_rate"])
                    minimum_balance = to_float(row["minimum_balance"])
                    management_fee = to_float(row["management_fee"])

                    # Instantiate the correct BankAccount subclass
                    if acc_type == "ChequingAccount":
                        account_obj = ChequingAccount(
                            acc_num, client_num, balance,
                            date_created, overdraft_limit, overdraft_rate
                        )

                    elif acc_type == "InvestmentAccount":
                        account_obj = InvestmentAccount(
                            acc_num, client_num, balance,
                            date_created, management_fee
                        )

                    elif acc_type in ("SavingsAccount", "SavingAccount"):
                        account_obj = SavingAccount(
                            acc_num, client_num, balance,
                            date_created, minimum_balance
                        )

                    else:
                        # Invalid account type → raise error so it gets logged
                        raise ValueError("Not a valid account type.")

                    # Ensure account references an existing client
                    if client_num not in client_listing:
                        logging.error(
                            f"Bank Account {acc_num} contains invalid Client Number {client_num}")
                        # skip adding the account
                        continue  

                    # Store the account using account_number as key
                    accounts[acc_num] = account_obj

                except Exception as e:
                    # Log any error related to individual account creation
                    logging.error(f"Unable to create bank account: {e}")

    except Exception as e:
        logging.error(f"Error reading accounts.csv: {e}")

    # RETURN BOTH DICTIONARIES
    return client_listing, accounts

def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")