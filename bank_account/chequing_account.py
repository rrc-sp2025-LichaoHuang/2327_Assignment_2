
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from abc import ABC, abstractmethod
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
            if overdraft_limit >= 0:
                raise ValueError("Overdraft limit must less than 0.")
            self.__overdraft_limit = overdraft_limit
        else:
            raise ValueError("Overdraft limit must be numeric.")
        
        if isinstance(overdraft_rate, float):
            self.__overdraft_rate = overdraft_rate
        else:
            raise ValueError("Overdraft rate must be numeric.")


    def __str__(self) -> str:
        """
        
        """
        return (
            super().__str__()
            + f"Overdraft limit: ${self.__overdraft_limit:,.2f} "
            + f"Overdraft rate: {self.__overdraft_rate * 100:.2f}% "
            + "Account Type: Chequing"
        )
    
    @property
    def get_service_charges(self) -> float:
        if self.__balance < self.__overdraft_limit:
            service_fee = self.BASE_SERVICE_CHARGE + \
            (self.__overdraft_limit - self.__balance) * self.__overdraft_rate
        else:
            service_fee = self.BASE_SERVICE_CHARGE
        return service_fee