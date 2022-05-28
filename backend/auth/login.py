from getpass import getpass
from hashlib import pbkdf2_hmac
import utils.logger as logger
import colorama
import pymongo
from utils.functions import find_user, valid_input


def compare_hash(salt: str,
                 password_hash: str,
                 raw_password: str) -> int:
    if password_hash == pbkdf2_hmac('sha256', 
                                    raw_password.encode(), 
                                    salt.encode(), 
                                    500000).hex():
        return 0
    return 1
    

def login() -> dict or None:
    '''
    Main entry point function for the login module.
    '''
    username = input("Please enter your username:\n> ")
    
    # Try to get the user from the collection
    user_doc = find_user(username)
    
    # Return 1 if the user doesn't exist
    if user_doc is None:
        print(f"Username or student ID is not registered."
                + " Please register an account to continue.")
        return None
    
    for trial in range(1, 4):
        password = valid_input("Please enter your password:\n> ",
                               lambda x: x,
                               "Your password is empty, please try again.",
                               True)
            
        if compare_hash(user_doc["salt"],
                        user_doc["password_hash"],
                        password):
            if trial == 3:
                logger.warning(f"User {username} has exceeded maximum login attempts.")
                print(f"Password incorrect, exiting... (try {trial}/3)")
                return None
            print(f"Password incorrect, please try again. (try {trial}/3)")

        else:
            logger.logger().info(f"User {username} has logged in.")
            print(f"Login success! Welcome {username}.")
            return user_doc

if __name__ == "__main__":
    login()
