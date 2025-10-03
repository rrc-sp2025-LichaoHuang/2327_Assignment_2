
__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    Represents an investment account with a management fee.

    Inherits from BankAccount and applies a management fee unless 
    the account has existed for over 10 years, in which case the fee is waived.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days = int(10 * 365.25))

    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        Initialize an InvestmentAccount instance with a management fee.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client identifier.
            balance (float): Initial account balance.
            date_created (date): Account creation date.
            management_fee (float): Additional management fee for the account.
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55
        
    
    def __str__(self) -> str:
        """
        Return a string representation of the investment account.

        Includes base account info, management fee (or 'Waived' if account older than 10 years), 
        and account type.
        """
        # account_duration = (self._date_created - self.TEN_YEARS_AGO)
        # duration_year = account_duration.days / 365.25
        # if duration_year >= 10:
        if self._date_created < self.TEN_YEARS_AGO:
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


    def get_service_charges(self) -> float:
        """
        Calculate the service charges for this investment account.

        Returns:
            float: Base service charge plus management fee if applicable.
        """
       # account_duration = (self._date_created - self.TEN_YEARS_AGO)
       # duration_year = account_duration.days / 365.25
        # if duration_year >= 10:
        if self._date_created < self.TEN_YEARS_AGO:
            service_fee = self.BASE_SERVICE_CHARGE
        else:
            service_fee = self.BASE_SERVICE_CHARGE + self.__management_fee
        return service_fee