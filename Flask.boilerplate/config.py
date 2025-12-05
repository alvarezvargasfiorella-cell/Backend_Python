import os
from dotenv import load_dotenv

load_dotenv()

class config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    