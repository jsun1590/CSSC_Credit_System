import logging
from getpass import getpass
from hashlib import pbkdf2_hmac

import colorama
import pymongo
from src.utils.functions import find_user, valid_input


def compare_hash(salt: str,
                 password_hash: str,
                 raw_password: str) -> int:
    if password_hash == pbkdf2_hmac('sha256', 
                                    raw_password.encode(), 
                                    salt.encode(), 
                                    500000).hex():
        return 0
    return 1
    

def login():
    '''
    Main entry point function for the login module.
    '''
    user = input("Please enter your username or student id:\n> ")
    
    # Try to get the user from the collection
    user_doc = find_user(user, user)
    
    # Return 1 if the user doesn't exist
    if user_doc is None:
        print(f"Username or student ID is not registered."
                + " Please register an account to continue.")
        return 1
    
    password = valid_input("Please enter your password:\n> ", 
                               lambda x: x,
                               "Your password is empty, please try again.",
                               True)

    
    if compare_hash(user_doc["salt"],
                        user_doc["password_hash"],
                        password):
        print("Password incorrect, please try again.")
        return 1

    return user_doc

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    login()
