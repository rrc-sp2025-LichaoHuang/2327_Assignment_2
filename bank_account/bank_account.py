

__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from abc import ABC, abstractmethod

class BankAccount(ABC):
    """
    Abstract base class for a bank account.

    Stores account number, client number, balance, and creation date.
    Provides deposit, withdraw, and balance update methods.
    Subclasses must implement get_service_charges().

    """

    BASE_SERVICE_CHARGE: float = 0.50

    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date):
        """
        Initialize a BankAccount instance with account number, client number, balance, 
        and creation date.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client identifier.
            balance (float): Initial balance.
            date_created (date): Account creation date.

        Raises:
            ValueError: If account_number or client_number is not an int.
            TypeError: If balance cannot be converted to a float.
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number should be an int.")
        

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number should be an int.")
        

        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()


    @property
    def account_number(self):
        """
        Get the account number.

        Returns:
            int: The unique account number.
        """
        return self.__account_number

    @property
    def client_number(self):
        """
        Get the client number.

        Returns:
            int: The client identifier linked to this account.
        """
        return self.__client_number

    @property
    def balance(self):
        """
        Get the current account balance.

        Returns:
            float: The balance of the account.
        """
        return self.__balance
    

    def update_balance(self, amount: float) -> None:
        """
        Update the account balance by adding the given numeric amount.

        Args:
            amount (float): The amount to add (can be positive or negative).
        """
        if isinstance(amount,(int,float)):
            self.__balance += float(amount)
        else:
            pass


    def deposit(self, amount: float) -> None:
        """
        Deposit a positive numeric amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            TypeError: If amount is not numeric.
            ValueError: If amount is not positive.
        """
        if isinstance(amount, (float,int)):
            if amount <= 0:
                raise ValueError(f"Deposit amount: ${(amount):,.2f} must be positive.")
            else:
                self.update_balance(amount)
        else:
            raise TypeError(f"Deposit amount: {amount} must be numeric.")
        

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a positive numeric amount from the account if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            TypeError: If amount is not numeric.
            ValueError: If amount is non-positive or exceeds the balance.
        """
        if isinstance(amount, (float, int)):
            if amount <= 0:
                raise ValueError(f"Withdraw amount: ${(amount):,.2f} must be positive.")
            if amount > self.__balance:
                raise ValueError(f"Withdraw amount: ${(amount):,.2f}"
                                 f"must not exceed the account balance: \
                                    ${(self.__balance):,.2f}.")
            self.update_balance(-amount)
        else:
            raise TypeError(f"Withdraw amount: {amount} must be numeric.")
        

    def __str__(self) -> str:
        """
        return:
                "Account Number:(account_number) Balance: $(balance)"
        """
        return (
                f"Account Number: {self.__account_number} "
                f"Balance: ${self.__balance:,.2f} "
                f"Date Created: {self._date_created} \n"
            )
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Undefined abstract method to get service charges.

        """
        pass