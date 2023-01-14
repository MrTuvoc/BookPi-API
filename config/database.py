from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/etc/secrets/.env')
load_dotenv(dotenv_path=dotenv_path)

username = environ.get("DBUSER")
password = environ.get("DBPASS")

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.6ahdmfc.mongodb.net/?retryWrites=true&w=majority")
db = client["bookpidb"]
collection_name = db["bookpicol"]