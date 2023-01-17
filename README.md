
# BookPi

Unlock a world of knowledge with our powerful book retrieval API. Discover a vast collection of books from various genres.

BookPi is a CRUD REST API made with FastAPI in python.
## Documentation
BookPi is deployed to Render.com, You can use it and find documentation on
[BookPI](https://bookpi.onrender.com/)


## Technologies

- Python
- FastAPI
- MongoDB
- Render
- CRUD REST API


## Run Locally for Development

Clone the project

```
  git clone https://github.com/MrTuvoc/BookPi
  cd BookPi
```

Create a .env file in /etc/secrets/
```
  DBUSER = MongoDB username
  DBPASS = MongoDB password
  DBNAME = MongoDB database name
  COLNAME = MongoDB collection name
```
Or just change the code in config/database.py to suit your needs

Create a python virtual environment and actiavte it
```
  python -m venv venv
  source venv/bin/activate
```
Install dependencies

```
  pip install -r requirements.txt
```

Start the server

```
  uvicorn BookPi:app --reload
```

Access the server

  - http://localhost:8000