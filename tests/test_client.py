"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client

class TestCourse(unittest.TestCase):
    def test_init_valid_inputs_attributes_set(self):
        # Arrange and Act
        testclient = Client(123,"Richard","Huang","RH@rrc.ca")

        # Assert
        self.assertEqual(123,testclient._Client__client_number)
        self.assertEqual("Richard",testclient._Client__first_name)
        self.assertEqual("Huang",testclient._Client__last_name)
        self.assertEqual("RH@rrc.ca",testclient._Client__email_address)


    def test_init_invalid_client_number_input(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            testclient = Client("aaa","Richard","Huang","RH@rrc.ca")

    
    def test_init_enpty_first_name_input(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            testclient = Client(123,"","Huang","RH@rrc.ca")


    def test_init_invalid_last_name_input(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            testclient = Client(123,"Richard","","RH@rrc.ca")


    def test_init_invalid_email_address_input(self):
        # Arrange and Act
        testclient = Client(123,"Richard","Huang","RHrrc.ca")

        # Assert
        self.assertEqual("email@pixell-river.com",testclient._Client__email_address)