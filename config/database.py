from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/etc/secrets/.env')
load_dotenv(dotenv_path=dotenv_path)

username = getenv("DBUSER")
password = getenv("DBPASS")

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.6ahdmfc.mongodb.net/bookpidb?retryWrites=true&w=majority")
db = client.bookpidb
collection_name = db["bookpicol"]