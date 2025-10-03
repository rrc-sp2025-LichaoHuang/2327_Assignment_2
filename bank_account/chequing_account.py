
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    Represents a chequing account with overdraft facility.

    Inherits from BankAccount and adds overdraft limit and rate.
    Calculates service charges considering overdraft usage.
    """

    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initialize a ChequingAccount instance with overdraft settings.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client identifier.
            balance (float): Initial balance.
            date_created (date): Account creation date.
            overdraft_limit (float): Allowed overdraft limit (negative value).
            overdraft_rate (float): Rate applied on overdraft used.
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
        Return a string representation of the chequing account,
        including base info, overdraft limit and rate, and account type.
        """
        return (
            super().__str__()
            + f"Overdraft limit: ${self.__overdraft_limit:,.2f} "
            + f"Overdraft rate: {self.__overdraft_rate * 100:.2f}% "
            + "Account Type: Chequing"
        )
    
    def get_service_charges(self) -> float:
        """
        Calculate the service charges for this chequing account.

        Returns:
            float: Base service charge plus additional fees if balance is below overdraft limit.
        """
        if self.balance < self.__overdraft_limit:
            service_fee = self.BASE_SERVICE_CHARGE + \
            (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        else:
            service_fee = self.BASE_SERVICE_CHARGE
        return service_fee