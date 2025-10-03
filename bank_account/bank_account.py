

__author__ = "Lichao Huang"
__version__ = "1.0.0"

from datetime import date
from abc import ABC, abstractmethod

class BankAccount(ABC):
    """
    
    """
    def __init__(self, account_number : int, client_number: int, balance: float,
                 date_created: date):
        """
        Initialize a Bank account instance.
        Args:
            account_number(int): Account number.
            client_number(int): Client number.
            balance(str): Account balance.
            date_created (date): Account create date.

        Returns:
            None
            
        Raises:
            ValueError: 
                Account_number is not int.
                Client_number is not int.
                Balance is not numeric.
            TypeError:
                Balance is not float or int.
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
        # Return account number.
        return self.__account_number

    @property
    def client_number(self):
        # Return client number.
        return self.__client_number

    @property
    def balance(self):
        # Return account balance.
        return self.__balance
    

    def update_balance(self, amount: float) -> None:
        # Update balance to a specific value.
        if isinstance(amount,(int,float)):
            self.__balance = float(amount)
        else:
            raise ValueError


    def deposit(self, amount: float) -> None:
        # Make deposit when amount is numeric and it is a positive number.
        if isinstance(amount, (float,int)):
            if amount <= 0:
                raise ValueError(f"Deposit amount: ${abs(amount):,.2f} must be positive.")
            else:
                self.__balance += float(amount)
        else:
            raise TypeError(f"Deposit amount: {amount} must be numeric.")
        

    def withdraw(self, amount: float) -> None:
        # Make a withdraw when amount is numeric and it is a positive number 
        # and the account has sufficient balance.
        if isinstance(amount, (float, int)):
            if amount <= 0:
                raise ValueError(f"Withdraw amount: ${abs(amount):,.2f} must be positive.")
            if amount > self.__balance:
                raise ValueError(f"Withdraw amount: ${abs(amount):,.2f}"
                                 f"must not exceed the account balance: ${abs(self.__balance):,.2f}.")
            self.__balance -= float(amount)
        else:
            raise TypeError(f"Withdraw amount: {amount} must be numeric.")
        

    def __str__(self) -> str:
        """
        return:
                "Account Number:(account_number) Balance: $(balance)"
        """
        return (f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Undefined abstract method to get service charges.

        """
        pass