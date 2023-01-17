from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/etc/secrets/.env')
load_dotenv(dotenv_path=dotenv_path)

username = environ.get("DBUSER")
password = environ.get("DBPASS")
dbname = environ.get("DBNAME")
col_name = environ.get("COLNAME")

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.4di2bdx.mongodb.net/?retryWrites=true&w=majority")
db = client[dbname]
collection_name = db[col_name]