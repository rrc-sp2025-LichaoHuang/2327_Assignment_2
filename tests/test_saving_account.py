from bank_account.bank_account import BankAccount
import unittest
from bank_account.saving_account import SavingAccount
from datetime import date


class TestInvestmentAccount(unittest.TestCase):

    def test_init_sets_attributes_with_valid_inputs(self):
        account = SavingAccount(123,321,-50, date(2000,10,10), 10)

        self.assertEqual(123, account._BankAccount__account_number)
        self.assertEqual(321, account._BankAccount__client_number)
        self.assertEqual(-50, account._BankAccount__balance)
        self.assertEqual(date(2000,10,10), account._date_created)
        self.assertEqual(10, account._SavingAccount__minimum_balance)

    def test_init_sets_attributes_with_invalid_minimum_balance_get_default_minimum(self):
        account = SavingAccount(123,321,-50, date(2000,10,10), "aa")

        self.assertEqual(50, account._SavingAccount__minimum_balance)

    def test_get_service_charges_balance_greater_than_the_minimum_get_get_only_BASE_SERVICE_CHARGE(self):
        account = SavingAccount(123,321, 100, date(1000,10,10), 50)
        
        service_fee = account.get_service_charges()

        self.assertEqual(0.50, service_fee)

    def test_get_service_charges_balance_equal_than_the_minimum_get_get_only_BASE_SERVICE_CHARGE(self):
        account = SavingAccount(123,321, 50, date(1000,10,10), 50)
        
        service_fee = account.get_service_charges()

        self.assertEqual(0.50, service_fee)

    def test_get_service_charges_balance_less_than_the_minimum_get_get_only_BASE_SERVICE_CHARGE(self):
        account = SavingAccount(123,321, 40, date(1000,10,10), 50)
        
        service_fee = account.get_service_charges()

        self.assertEqual(1.0, service_fee)

    def test_str_valid_input_returns_expected_string(self):
        account = SavingAccount(123,321,-50, date(2020,10,10), 50)

        str_return = account.__str__()

        expect = ("Account Number: 123 Balance: $-50.00 "
                "Date Created: 2020-10-10 \nMinimum Balance: $50.00 Account Type: Savings")
        
        self.assertEqual(str_return, expect)

