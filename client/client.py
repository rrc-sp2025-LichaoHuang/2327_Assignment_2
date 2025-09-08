

from email_validator import validate_email, EmailNotValidError


__author__ = "Lichao Huang"
__version__ = "1.0.0"


class client:
    def __init__(self,client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Args:
            client_number(int): Client number of this client.
            first_name(str): First name of this client.
            last_name(str): Last name of this client
            email_address(str): E-mail address of this client.

        Returns:
            None
        Raises:
            ValueError: 
                client_number is not int.
                first_name is blank.
                last_name is blank.
            EmailNotValidError:
                email_address is not valid.
        """
        if client_number is int:
            self.__client_number = client_number
        else:
            raise ValueError("Client number should be an int.")
        
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")
        

        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")
        

        try:
            self.__email_address = validate_email(email_address, check_deliverability= False)
        except EmailNotValidError as e:
            self.__email_address = "email@pixell-river.com"
            print(f"Error:{e}")

    @property
    # Return the client number of this client.
    def client_number(self) -> int:
        return self.__client_number
    

    @property
    # Return the first name of this client.
    def first_name(self) -> str:
        return self.__first_name
    

    @property
    # Return the last name of this client.
    def last_name(self) -> str:
        return self.__last_name
    

    @property
    # Return the email address of this client.
    def email_address(self) -> str:
        return self.__email_address
    
    
    def __str__(self) -> str:
        """
        return:
            All information of this client.
            Client Number:
            First Name:
            Last Name:
            E-mail Address:

        """
        return(f"Client Number:{self.__client_number}"
               +f"\nFirst Name:{self.__first_name}"
               +f"\nLast Name:{self.__last_name}"
               +f"\nE-mail Address:{self.__email_address}")

        