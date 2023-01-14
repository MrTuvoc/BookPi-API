from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
from pathlib import Path
import urllib.parse

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

username = urllib.parse.quote_plus(getenv("DBUSER"))
password = urllib.parse.quote_plus(getenv("DBPASS"))

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.6ahdmfc.mongodb.net/bookpidb?retryWrites=true&w=majority")
db = client.bookpidb
collection_name = db["bookpicol"]