__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):
    """
    Represents an investment account with a management fee.

    Inherits from BankAccount and applies a management fee unless 
    the account has existed for over 10 years, in which case the fee is waived.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=int(10 * 365.25))

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        Initialize an InvestmentAccount instance with a management fee.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client identifier.
            balance (float): Balance.
            date_created (date): Account creation date.
            management_fee (float): Additional management fee for the account.

        Notes:
            If the management_fee cannot be converted to a numeric value,
            a default value of 2.55 will be used instead.
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except Exception:
            self.__management_fee = 2.55

        # Negative management fees are not allowed.
        # The test cases expect default behavior rather than exception raising.
        if self.__management_fee < 0:
            self.__management_fee = 2.55

        # Create an instance of ManagementFeeStrategy.
        # This object will handle the calculation of service charges.
        # It uses the account's creation date and management fee rate
        # to determine whether a fee should be applied or waived.
        self.__service_charge_strategy = ManagementFeeStrategy(
            date_created, self.__management_fee
        )

        # Keep a copy of the creation date for display and comparison.
        self.__date_created_copy = date_created

    def __str__(self) -> str:
        """
        Return a string representation of the investment account.

        Includes base account info, management fee (or 'Waived' if account older than 10 years), 
        and account type.
        """
        if self.__date_created_copy <= self.TEN_YEARS_AGO:
            return (
                super().__str__()
                + "Management fee: Waived Account "
                + "Account Type: Investment"
            )
        else:
            return (
                super().__str__()
                + f"Management fee: ${self.BASE_SERVICE_CHARGE + self.__management_fee:.2f} "
                + "Account Type: Investment"
            )

    def get_service_charges(self) -> float:
        """
        Calculate the service charges for this investment account.

        Returns:
            float: Base service charge plus management fee if applicable.

        Notes:
            Accounts older than ten years are charged only the base fee.
            Accounts younger than ten years include the management fee
            in addition to the base service charge.
        """
        if self.__date_created_copy <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee