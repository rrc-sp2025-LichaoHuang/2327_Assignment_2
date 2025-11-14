__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Main window that lets the user search for a client by client number.
    Once a client is found, their bank accounts will show in the table.
    The user can then click an account to open the Account Details window.
    """

    def __init__(self):
        """Set up the UI, load the CSV data, and connect all the signals."""
        super().__init__()

        # Load client and account dictionaries from CSV files
        self.client_listing, self.accounts = load_data()

        # Hook up buttons and widgets to their event-handling methods
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)

    # ------------------------------------------------------------------
    def on_lookup_client(self):
        """
        Runs when the user clicks the 'Lookup Client' button.

        This method:
        - Reads the typed client number
        - Validates it
        - Looks up the client in the dictionary
        - Shows the client's name
        - Lists all matching accounts in the table
        """

        # Clear old table data every time we do a fresh lookup
        self.account_table.setRowCount(0)
        self.client_info_label.setText("")

        text = self.client_number_edit.text().strip()

        # Try converting text input → integer
        # If this fails, the user typed something that isn't a number
        try:
            client_number = int(text)
        except ValueError:
            QMessageBox.information(
                self,
                "Input Error",
                "The client number must be a numeric value."
            )
            self.reset_display()
            return

        # Check if the client actually exists in our dictionary
        if client_number not in self.client_listing:
            QMessageBox.information(
                self,
                "Not Found",
                f"Client number: {client_number} not found."
            )
            self.reset_display()
            return

        # At this point, we have a valid client
        client = self.client_listing[client_number]

        # Show the client's full name in the label
        self.client_info_label.setText(
            f"Client Name: {client.first_name}  {client.last_name}"
        )

        # Now display all accounts that belong to this client
        row = 0
        for account in self.accounts.values():
            if account.client_number == client_number:

                # Add a new row to the table
                self.account_table.insertRow(row)

                # Account Number
                item_acc = QTableWidgetItem(str(account.account_number))
                item_acc.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, 0, item_acc)

                # Balance
                item_bal = QTableWidgetItem(f"${account.balance:,.2f}")
                item_bal.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, 1, item_bal)

                # Date Created
                item_date = QTableWidgetItem(str(account._date_created))
                item_date.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, 2, item_date)

                # Account Type
                item_type = QTableWidgetItem(account.__class__.__name__)
                item_type.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, 3, item_type)

                row += 1

        # Auto-adjust column sizes so text is not cut off
        self.account_table.resizeColumnsToContents()

    # ------------------------------------------------------------------
    def on_text_changed(self):
        """
        Runs every time the user types something in the client number box.

        Purpose:
        - Clear old table data
        - Clear the client name label
        So the user always gets a clean slate.
        """
        self.account_table.setRowCount(0)
        self.client_info_label.setText("")

    # ------------------------------------------------------------------
    def on_select_account(self, row: int, column: int):
        """
        Runs when the user clicks on any cell in the account table.

        Steps:
        - Read the account number from the row
        - Validate it
        - Find the BankAccount object
        - Open the Account Details window
        """

        # Get the account number from the first column
        item = self.account_table.item(row, 0)

        # If nothing is selected or row is weird, show a warning
        if item is None:
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return

        text = item.text().strip()
        if not text:
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return

        # Convert account number to int
        try:
            account_number = int(text)
        except ValueError:
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return

        # Check if this account exists
        if account_number not in self.accounts:
            QMessageBox.information(self, "No Bank Account", "Bank Account selected does not exist.")
            return


        

        # Everything is valid → open the Account Details dialog
        account = self.accounts[account_number]
        window = AccountDetailsWindow(account)
        window.balance_updated.connect(self.save_account_changes)
        window.exec()

    def save_account_changes(self, updated_account: BankAccount):
        """
        This method is called when the AccountDetailsWindow emits balance_updated.
        It writes the updated account info back into the CSV file and refreshes the table.
        """
        # Write the updated account to CSV
        update_data(updated_account)

        # Refresh table output so balance updates instantly
        self.on_lookup_client()