__author__ = "Lichao Huang"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account import *

class ServiceChargeStrategy(ABC):
    """
    Abstract base class for all service charge strategies.
    Defines the interface for calculating service charges.
    """

    BASE_SERVICE_CHARGE = 0.50
    @abstractmethod
    def calculate_service_charges(self, account: BankAccount):
        """
        Calculate the service charges for the given account.
        This method must be implemented by all subclasses.
        """
        pass