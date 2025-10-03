
from bank_account.bank_account import BankAccount
import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date


class TestChequingAccount(unittest.TestCase):

    def test_init_sets_attributes_with_valid_inputs(self):
        account = ChequingAccount(123,321,-50, date(2000,10,10), -10.0, 0.1)

        self.assertEqual(123, account._BankAccount__account_number)
        self.assertEqual(321, account._BankAccount__client_number)
        self.assertEqual(-50, account._BankAccount__balance)
        self.assertEqual(date(2000,10,10), account._date_created)
        self.assertEqual(-10, account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.1, account._ChequingAccount__overdraft_rate)

    def test_get_service_charges_large_balance_less_fee(self):
        account = ChequingAccount(123,321,500, date(2000,10,10), -10.0, 0.1)
        service_charges = account.get_service_charges()
        self.assertEqual(0.50, service_charges)

    def test_init_set_overdraft_limit_invalid_return_default_limit(self):
        account = ChequingAccount(123,321,-50, date(2000,10,10), "aaa", 0.1)

        self.assertEqual(-100, account._ChequingAccount__overdraft_limit)


    def test_init_set_overdraft_rate_invalid_return_default_limit(self):
        account = ChequingAccount(123,321,-50, date(2000,10,10), -10.0, "aaa")

        self.assertEqual(0.05, account._ChequingAccount__overdraft_rate)


    def test_init_set_created_date_invalid_return_today_as_created_date(self):
        account = ChequingAccount(123,321,-50, "aaa", -10.0, 0.1)

        self.assertEqual(date(2025, 10, 3), account._date_created)

    def test_str_valid_input_returns_expected_string(self):

        account = ChequingAccount(123,321,-50, date(2000,10,10), -10.0, 0.1)
        str_return = account.__str__()
        expect = ("Account Number: 123 Balance: $-50.00 "
                "Date Created: 2000-10-10 \nOverdraft limit: $-10.00 "
                "Overdraft rate: 10.00% Account Type: Chequing")
        self.assertEqual(str_return, expect)

    def test_get_service_charges_balance_greater_than_limit_get_only_BASE_SERVICE_CHARGE(self):
        account = ChequingAccount(123,321, 50, date(2000,10,10), -10.0, 0.1)
        
        service_fee = account.get_service_charges()

        self.assertEqual(0.50, service_fee)


    def test_get_service_charges_balance_equal_than_limit_get_only_BASE_SERVICE_CHARGE(self):
        account = ChequingAccount(123,321, -10, date(2000,10,10), -10.0, 0.1)
        
        service_fee = account.get_service_charges()

        self.assertEqual(0.50, service_fee)

    def test_get_service_charges_balance_less_than_limit_get_extra_fee(self):
        account = ChequingAccount(123,321, -20, date(2000,10,10), -10.0, 0.1)
        
        service_fee = account.get_service_charges()

        self.assertEqual(1.5, service_fee)