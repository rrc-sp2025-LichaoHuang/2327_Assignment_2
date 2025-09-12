"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
from bank_account.bank_account import Bank_account
import unittest

class TestCourse(unittest.TestCase):
    
    # init test
    
    def test_init_valid_input_attributes_set(self):
        # Arrange and Act
        account = Bank_account(123,321,100001.1111)

        # Assert
        self.assertEqual(123,account._Bank_account__account_number)
        self.assertEqual(321,account._Bank_account__client_number)
        self.assertAlmostEqual(100001.1111, account._Bank_account__balance, places=4)


    def test_init_incalid_input_account_number(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            account = Bank_account("aaa",321,100001.1111)

    def test_init_invalid_input_client_number(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            account = Bank_account(123,"KFC",100001.1111)

    def test_init_invalid_input_balance(self):
        # Arrange and Act
        account = Bank_account(123,321,"BBB")

        # Assert
        self.assertEqual(0,account._Bank_account__balance)


    # deposit tests

    def test_deposit_valid(self):
        account = Bank_account(1, 1, 100)
        account.deposit(50)
        self.assertAlmostEqual(150, account._Bank_account__balance)

    def test_deposit_negative(self):
        account = Bank_account(1, 1, 100)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_deposit_non_numeric(self):
        account = Bank_account(1, 1, 100)
        with self.assertRaises(TypeError):
            account.deposit("abc")


    # withdraw tests

    def test_withdraw_valid(self):
        account = Bank_account(1, 1, 100)
        account.withdraw(40)
        self.assertAlmostEqual(60, account._Bank_account__balance)

    def test_withdraw_exceed_balance(self):
        account = Bank_account(1, 1, 100)
        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_withdraw_negative(self):
        account = Bank_account(1, 1, 100)
        with self.assertRaises(ValueError):
            account.withdraw(-50)

    def test_withdraw_non_numeric(self):
        account = Bank_account(1, 1, 100)
        with self.assertRaises(TypeError):
            account.withdraw("abc")


    # update_balance tests

    def test_update_balance_valid(self):
        account = Bank_account(1, 1, 100)
        account.update_balance(500.55)
        self.assertAlmostEqual(500.55, account._Bank_account__balance)

    def test_update_balance_non_numeric(self):
        account = Bank_account(1, 1, 100)
        with self.assertRaises(ValueError):
            account.update_balance("abc")

    # accessors tests


    def test_account_number_accessor(self):
        account = Bank_account(123, 456, 789.0)
        self.assertEqual(123, account.account_number)

    def test_client_number_accessor(self):
        account = Bank_account(123, 456, 789.0)
        self.assertEqual(456, account.client_number)

    def test_balance_accessor(self):
        account = Bank_account(123, 456, 789.0)
        self.assertAlmostEqual(789.0, account.balance, places=2)

 
    # __str__ test
    
    def test_str_output_format(self):
        account = Bank_account(12345, 67890, 1500.756)
        expected_str = "Account Number: 12345 Balance: $1500.76"
        self.assertEqual(str(account), expected_str)