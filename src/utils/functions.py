from getpass import getpass

from pymongo import MongoClient
from src.configs import config


def valid_input(
    prompt: str,
    validator = lambda x: True,
    error: str = "Invalid input, please try again.",
    hidden: bool = False
) -> str:
    '''
    Keeping taking user inputs until the validator function returns True.
    '''
    while not validator(value := getpass(prompt) if hidden else input(prompt)):
        print(error)
    return value

def find_user(username: str, student_id: str = "") -> dict or None:
    client = MongoClient(config.DB_IP, config.DB_PORT)
    db = client.credit_db
    users = db.users
    query = users.find_one({"$or":
        [{"student_id": student_id},
         {"username": username}]})
    return query
