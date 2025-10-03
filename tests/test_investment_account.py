from bank_account.bank_account import BankAccount
import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date


class TestInvestmentAccount(unittest.TestCase):

    def test_init_sets_attributes_with_valid_inputs(self):
        account = InvestmentAccount(123,321,-50, date(2000,10,10), 1)

        self.assertEqual(123, account._BankAccount__account_number)
        self.assertEqual(321, account._BankAccount__client_number)
        self.assertEqual(-50, account._BankAccount__balance)
        self.assertEqual(date(2000,10,10), account._date_created)
        self.assertEqual(1, account._InvestmentAccount__management_fee)

    def test_init_sets_attributes_with_invalid_management_fee_get_default_number(self):
        account = InvestmentAccount(123,321,-50, date(2000,10,10), "a")

        self.assertEqual(2.55, account._InvestmentAccount__management_fee)

    def test_get_service_charges_duration_older_than_ten_get_get_only_BASE_SERVICE_CHARGE(self):
        account = InvestmentAccount(123,321, 50, date(1000,10,10), 1)
        
        service_fee = account.get_service_charges()

        self.assertEqual(0.50, service_fee)

    def test_get_service_charges_duration_equal_than_ten_get_get_only_BASE_SERVICE_CHARGE(self):
        account = InvestmentAccount(123,321, 50, date(2015,10,3), 1)
        
        service_fee = account.get_service_charges()

        self.assertEqual(0.50, service_fee)

    def test_get_service_charges_duration_less_than_ten_get_get_only_BASE_SERVICE_CHARGE(self):
        account = InvestmentAccount(123,321, 50, date(2025,10,3), 1)
        
        service_fee = account.get_service_charges()

        self.assertEqual(1.5, service_fee)

    def test_str_valid_input_account_elder_than_10_years_returns_expected_string(self):
        account = InvestmentAccount(123,321,-50, date(2000,10,10), 1)

        str_return = account.__str__()

        expect = ("Account Number: 123 Balance: $-50.00 "
                "Date Created: 2000-10-10 \nManagement fee: Waived Account Account Type: Investment")
        
        self.assertEqual(str_return, expect)

    def test_str_valid_input_account_younger_than_10_years_returns_expected_string(self):
        account = InvestmentAccount(123,321,-50, date(2020,10,10), 1)

        str_return = account.__str__()

        expect = ("Account Number: 123 Balance: $-50.00 "
                "Date Created: 2020-10-10 \nManagement fee: $1.50 Account Type: Investment")
        
        self.assertEqual(str_return, expect)
