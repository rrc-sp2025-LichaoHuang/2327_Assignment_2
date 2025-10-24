__author__ = "Lichao Huang"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract base class for all service charge strategies.
    """
    
    BASE_SERVICE_CHARGE = 0.50

    def calculate_service_charges(self, account):
            """
            Calculate the service charges for the given account.
            """
            pass