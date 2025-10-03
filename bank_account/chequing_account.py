
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """

    """

    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        
        """
        
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(overdraft_limit, float):
            self.__overdraft_limit = overdraft_limit
        else:
            self.__overdraft_limit = -100
        
        if isinstance(overdraft_rate, float):
            self.__overdraft_rate = overdraft_rate
        else:
            self.__overdraft_rate = 0.05


    def __str__(self) -> str:
        """
        
        """
        return (
            super().__str__()
            + f"Overdraft limit: ${self.__overdraft_limit:,.2f} "
            + f"Overdraft rate: {self.__overdraft_rate * 100:.2f}% "
            + "Account Type: Chequing"
        )
    
    def get_service_charges(self) -> float:
        """
        
        """
        if self.balance < self.__overdraft_limit:
            service_fee = self.BASE_SERVICE_CHARGE + \
            (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        else:
            service_fee = self.BASE_SERVICE_CHARGE
        return service_fee