
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy


class SavingAccount(BankAccount):
    """
    Represents a savings account with a minimum balance requirement.

    Inherits from BankAccount and applies higher service charges if 
    the balance falls below the minimum balance. The calculation is
    delegated to MinimumBalanceStrategy.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """
        Initialize a SavingAccount instance with a minimum balance requirement.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client identifier.
            balance (float): Balance.
            date_created (date): Account creation date.
            minimum_balance (float): Minimum balance to avoid premium service charges.

        Raises:
            ValueError: If minimum_balance cannot be converted to a float
                        or if it is negative.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # validate minimum_balance
        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50
            
        if self.__minimum_balance < 0:
            raise ValueError("minimum_balance cannot be negative.")

        # Strategy pattern integration
        # Assumes MinimumBalanceStrategy defines SERVICE_CHARGE_PREMIUM = 2.0 internally
        self.__service_charge_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def __str__(self) -> str:
        """
        Return a string representation of the savings account.

        Includes base account info, minimum balance, and account type.
        """
        return (
            super().__str__()
            + f"Minimum Balance: ${self.__minimum_balance:,.2f} "
            + "Account Type: Savings"
        )

    def get_service_charges(self) -> float:
        """
        Calculate the service charges for this savings account.

        Returns:
            float: Service charge calculated by MinimumBalanceStrategy.
        """
        return self.__service_charge_strategy.calculate_service_charges(self)