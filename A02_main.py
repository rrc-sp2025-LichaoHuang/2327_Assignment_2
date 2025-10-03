"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "Lichao Huang"
__version__ = "1.0.0"
__credits__ = "COMP-2327 (268395) Intermediate Software Development"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account_below_limit = ChequingAccount(123,321, -20, date(2000,10,10), -10.0, 0.1)

# 3. Print the ChequingAccount created in step 2.
print(chequing_account_below_limit.__str__())
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account_below_limit.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_account_below_limit.deposit(1000)
# 4b. Print the ChequingAccount
print(chequing_account_below_limit.__str__())
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account_below_limit.get_service_charges())

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
saving_account = SavingAccount(123,321, 100, date(1000,10,10), 50)

# 6. Print the SavingsAccount created in step 5.
print(saving_account.__str__())
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(saving_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
saving_account.withdraw(60)
# below the minimum balance.
# 7b. Print the SavingsAccount.
print(saving_account.__str__())
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(saving_account.get_service_charges())



print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account = InvestmentAccount(123,321, 50, date(2025,10,3), 1)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account.__str__())
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account_2 = InvestmentAccount(123,321, 50, date(1025,10,3), 1)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_account_2.__str__())
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_account_2.get_service_charges())

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
# 2
chequing_account_below_limit.withdraw(chequing_account_below_limit.get_service_charges())
# 5
saving_account.withdraw(saving_account.get_service_charges())
# 8
investment_account.withdraw(investment_account.get_service_charges())
# 10
investment_account_2.withdraw(investment_account_2.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing_account_below_limit.__str__())
print(saving_account.__str__())
print(investment_account.__str__())
print(investment_account_2.__str__())
