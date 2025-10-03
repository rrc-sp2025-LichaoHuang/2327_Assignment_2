
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount

class SavingAccount(BankAccount):
    """
    
    """

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """
        
        """
        
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50

    def __str__(self) -> str:
        """
        
        """
        return(
            super().__str__()
            + f"Minimum Balance: ${self.__minimum_balance:,.2f} "
            + "Account Type: Savings"

        )
    
    def get_service_charges(self) -> float:
        """
        
        """
        if self.balance > self.__minimum_balance:
            service_fee = self.BASE_SERVICE_CHARGE
        else:
            service_fee = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return service_fee