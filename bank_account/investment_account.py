
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    
    """

    TEN_YEARS_AGO = date.today() - timedelta(days = int(10 * 365.25))

    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55
        
    
    def __str__(self) -> str:
        account_duration = (self._date_created - self.TEN_YEARS_AGO)
        duration_year = account_duration.days / 365.25
        if duration_year >= 10:
            return(
                super().__str__()
                + "Management fee: Waived Account "
                + "Account Type: Investment"
            )
        else:
            return(
                super().__str__()
                + f"Management fee: ${self.BASE_SERVICE_CHARGE + self.__management_fee:.2f} "
                + "Account Type: Investment"
            )

    @property
    def get_service_charges(self) -> float:
        account_duration = (self._date_created - self.TEN_YEARS_AGO)
        duration_year = account_duration.days / 365.25
        if duration_year >= 10:
            service_fee = self.BASE_SERVICE_CHARGE
        else:
            service_fee = self.BASE_SERVICE_CHARGE + self.__management_fee
        return service_fee