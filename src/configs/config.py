import os

import dotenv

dotenv.load_dotenv()

DB_IP = os.getenv("DB_IP")
DB_PORT = int(os.getenv("DB_PORT"))
CONTACT_NAME = os.getenv("CONTACT_NAME")
