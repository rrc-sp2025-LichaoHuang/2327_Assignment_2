from datetime import date
from bank_account.saving_account import SavingAccount

acc1 = SavingAccount(3001, 4001, 800.0, date.today(), 1000.0)  # below minimum
print(acc1)
print("Service charges:", acc1.get_service_charges())

acc2 = SavingAccount(3002, 4002, 1500.0, date.today(), 1000.0) # above minimum
print(acc2)
print("Service charges:", acc2.get_service_charges())