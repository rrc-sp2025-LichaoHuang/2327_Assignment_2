
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
