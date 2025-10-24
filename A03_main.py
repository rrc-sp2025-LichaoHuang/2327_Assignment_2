"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "Lichao Huang"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from datetime import date
from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.saving_account import SavingAccount





# 2. Create a Client object with data of your choice.
client1 = Client(1, "Lichao", "Huang", "li@example.com")



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
account1 = ChequingAccount(1, client1.client_number, 500.00, date(2025, 1, 1), -100.0, 0.05)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

account2 = SavingAccount(2, client1.client_number, 150.00, date(2025, 1, 1), 50.0)



# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  


# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
account1.attach(client1)

# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
account2.attach(client1)





# 5a. Create a second Client object with data of your choice.

client2 = Client(2, "Alex", "Johnson", "alex@example.com")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
account3 = SavingAccount(3, client2.client_number, 200.00, date(2025, 1, 1), 50.0)
account3.attach(client2)




# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
try:
    account1.deposit(50)
    
    account1.deposit(15000)

    account1.withdraw(15450)
except Exception as e:
    print(e)

try:
    account2.deposit(25)
    account2.withdraw(150)
    account2.deposit(12000)
except Exception as e:
    print(e)

try:
    account3.withdraw(180)
    account3.deposit(20000)
except Exception as e:
    print(e)

