__author__ = "Lichao Huang"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges for savings accounts.
    Applies a premium charge if the balance falls below the minimum balance requirement.
    """

    SERVICE_CHARGE_PREMIUM = 2.0  # Premium multiplier for accounts below minimum balance

    def __init__(self, minimum_balance: float):
        """
        Initialize a MinimumBalanceStrategy instance with a specified minimum balance.

        Args:
            minimum_balance (float): The required minimum balance for standard service charges.

        Raises:
            ValueError: If minimum_balance cannot be converted to float or is negative.
        """
        try:
            self.__minimum_balance = float(minimum_balance)
        except Exception:
            raise ValueError("minimum_balance must be a numeric value.")
        if self.__minimum_balance < 0:
            raise ValueError("minimum_balance cannot be negative.")

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for an account using the minimum balance strategy.
        Implements the same logic as SavingsAccount.get_service_charges().

        Args:
            account (BankAccount): The account to calculate service charges for.

        Returns:
            float: The calculated service charge.
        """
        if account.balance >= self.__minimum_balance:
            service_fee = self.BASE_SERVICE_CHARGE
        else:
            service_fee = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return service_fee