import os
from dotenv import load_dotenv


load_dotenv()

class config:
    debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/dbname'