from threading import activeCount
import unittest
from  logic.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()
        
    def test_default_balance(self):
        self.assertEqual(self.account.get_balance(), "0.00",
                         "The default balance is incorrect.")
        
    def test_add_balance(self):
        self.account.add(500)
        self.account.add(500)
        self.account.add(50)
        self.account.add(5)
        self.assertEqual(self.account.get_balance(), "10.55",
                    "The account balance after adding credits is incorrect.")
        
    def test_remove_balance(self):
        self.account = Account(1000)
        self.account.remove(500)
        self.account.remove(50)
        self.account.remove(5)
        self.assertEqual(self.account.get_balance(), "4.45",
                    "The account balance after removing credits is incorrect.")
    
    def test_negative_balance(self):
        self.assertEqual(self.account.remove(500), -1,
            "The account is removing more credits than the balance available.")
        
        self.assertEqual(self.account.get_balance(), "0.00",
            "The account balance is negative.")
    
    def test_get_balance(self):
        self.account.add(500)
        self.account.remove(20)
        self.assertEqual(self.account.get_balance(), "4.80")