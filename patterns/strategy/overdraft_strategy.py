__author__ = "Lichao Huang"
__version__ = "1.0.0"


from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges related to overdraft accounts.
    Applies additional fees when the account balance is below the overdraft limit.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initialize an OverdraftStrategy instance with a limit and rate.

        Args:
            overdraft_limit (float): The allowed overdraft limit before extra charges apply.
            overdraft_rate (float): The rate charged on the amount below the overdraft limit.

        Raises:
            ValueError: If overdraft_limit or overdraft_rate cannot be converted to float,
                        or if either value is negative.
        """
        # Validate overdraft_limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except Exception:
            raise ValueError("overdraft_limit must be a numeric value.")
        if self.__overdraft_limit < 0:
            raise ValueError("overdraft_limit cannot be negative.")

        # Validate overdraft_rate
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except Exception:
            raise ValueError("overdraft_rate must be a numeric value.")
        if self.__overdraft_rate < 0:
            raise ValueError("overdraft_rate cannot be negative.")

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for an account using the overdraft strategy.
        Implements the same logic as the original ChequingAccount.get_service_charges().

        Args:
            account (BankAccount): The account to calculate service charges for.

        Returns:s
            float: The calculated service charge.
        """
        if account.balance < self.__overdraft_limit:
            service_fee = self.BASE_SERVICE_CHARGE + \
                          (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        else:
            service_fee = self.BASE_SERVICE_CHARGE
        return service_fee