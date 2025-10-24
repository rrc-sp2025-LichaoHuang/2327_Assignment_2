__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating management fee service charges.
    Used by investment accounts to determine if long-term accounts incur additional fees.
    """

    # Constant representing the date 10 years ago
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initialize a ManagementFeeStrategy instance with creation date and management fee.

        Args:
            date_created (date): The date the account was created.
            management_fee (float): The management fee rate applied to long-term accounts.

        Raises:
            ValueError: If management_fee cannot be converted to float or is negative.
        """
        self.__date_created = date_created

        try:
            self.__management_fee = float(management_fee)
        except Exception:
            raise ValueError("management_fee must be a numeric value.")
        if self.__management_fee < 0:
            raise ValueError("management_fee cannot be negative.")

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for an account using the management fee strategy.
        Implements the same logic as InvestmentAccount.get_service_charges().

        Args:
            account (BankAccount): The account to calculate service charges for.

        Returns:
            float: The calculated service charge.
        """
        if self.__date_created <= self.TEN_YEARS_AGO:
            service_fee = self.BASE_SERVICE_CHARGE + (account.balance * self.__management_fee)
        else:
            service_fee = self.BASE_SERVICE_CHARGE
        return service_fee