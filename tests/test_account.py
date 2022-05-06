from threading import activeCount
import unittest
from  logic.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()
        
    def test_default_balance(self):
        self.assertEqual(self.account.get_balance(), "0.00",
                         "THe default balance is incorrect.")
        
    def test_add_balance(self):
        self.account.add_balance(500)
        self.account.add_balance(500)
        self.account.add_balance(50)
        self.account.add_balance(5)
        self.assertEqual(self.account.get_balance(), "10.55",
                    "The account balance after adding balance is incorrect.")
        
    def test_remove_balance(self):
        self.account = Account(1000)
        self.account.remove_balance(500)
        self.account.remove_balance(50)
        self.account.remove_balance(5)
        self.assertEqual(self.account.get_balance(), "4.45",
                    "The account balance after removing balance is incorrect.")
    
    def test_negative_balance(self):
        self.assertEqual(self.account.remove_balance(500), -1,
            "The account is allowing more credits than the balance available to be removed.")
        
        self.assertEqual(self.account.get_balance(), "0.00",
            "The account balance is negative.")