
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount

class SavingAccount(BankAccount):
    """
    Represents a savings account with a minimum balance requirement.

    Inherits from BankAccount and applies higher service charges if 
    the balance falls below the minimum balance.
    """

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """
        Initialize a SavingAccount instance with a minimum balance requirement.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client identifier.
            balance (float): Balance.
            date_created (date): Account creation date.
            minimum_balance (float): Minimum balance to avoid premium service charges.
        """
        
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50

    def __str__(self) -> str:
        """
        Return a string representation of the savings account.

        Includes base account info, minimum balance, and account type.
        """
        return(
            super().__str__()
            + f"Minimum Balance: ${self.__minimum_balance:,.2f} "
            + "Account Type: Savings"

        )
    
    def get_service_charges(self) -> float:
        """
        Calculate the service charges for this savings account.

        Returns:
            float: Base service charge if balance meets minimum; otherwise, higher premium charge.
        """
        if self.balance >= self.__minimum_balance:
            service_fee = self.BASE_SERVICE_CHARGE
        else:
            service_fee = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return service_fee