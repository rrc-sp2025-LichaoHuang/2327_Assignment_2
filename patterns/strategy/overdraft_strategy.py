__author__ = "Lichao Huang"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


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
        """
        # Validate overdraft_limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except Exception:
            self.__overdraft_limit = -100.0

        # Validate overdraft_rate
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except Exception:
            self.__overdraft_rate = 0.05


        if self.__overdraft_rate < 0:
            self.__overdraft_rate = 0.05

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for an account using the overdraft strategy.
        Implements the same logic as the original ChequingAccount.get_service_charges().
        """
        if account.balance < self.__overdraft_limit:
            service_fee = self.BASE_SERVICE_CHARGE + \
                          (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        else:
            service_fee = self.BASE_SERVICE_CHARGE

        return service_fee