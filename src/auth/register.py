import logging
import secrets
from getpass import getpass
from hashlib import pbkdf2_hmac

import colorama
from pymongo import MongoClient
import src.configs.config as config
from src.utils.functions import find_user, valid_input


def salt_and_hash(raw_password: str) -> tuple[str, str]:
    '''
    Return a randomly generated hash and its corresponding hash of a password.
    '''
    salt = secrets.token_hex(8)
    password_hash = pbkdf2_hmac('sha256', raw_password.encode(), salt.encode(), 500000).hex()
    return salt, password_hash

def push_to_db(data: dict) -> int:
    '''
    Push a new user to the users collection
    '''
    client = MongoClient(config.DB_IP, config.DB_PORT)
    db = client.credit_db
    users = db.users
    users.insert_one(data)
    logger.info(f"New uesr {data['username']} created.")
    return 0

def register() -> int or dict:
    '''
    Main entry point funtion for the module
    '''
    student_id = valid_input("Please enter your student id:\n> ",
                             lambda x: x.isnumeric() and len(x) == 8,
                             "Invalid student id, please try again.")
    username = valid_input("Please enter a new username:\n> ",
                           lambda x: x,
                           "Your username is empty, please try again.")

    if find_user(student_id, username) is not None:
        print("Username or student ID is already registered."
              + f" Please contact {config.CONTACT_NAME} to reset your password if you have forgotten it.")
        return 1
    
    password_hash = None
    while password_hash is None:
        password = valid_input("Please enter a new password:\n> ", 
                               lambda x: x,
                               "Your password is empty, please try again.",
                               True)
        if password == getpass("Please enter your password again:\n> "):
            salt, password_hash = salt_and_hash(password)


    data = {
        "student_id": student_id,
        "username": username,
        "salt": salt,
        "password_hash": password_hash
    }


    push_to_db(data)
    return data

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    register()
