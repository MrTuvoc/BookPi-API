from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models.bookmodel import Book
from schemas.bookschema import books_serialize
from config.database import collection_name
from pymongo.errors import PyMongoError, ConnectionFailure
bookapirouter = APIRouter()

@bookapirouter.get("/status")
async def status():
    return {"status":"ok"}
# Retrieve all books
@bookapirouter.get("/")
async def getbooks():
    try:
        books = books_serialize(collection_name.find())
        return {"data":books}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=500, detail="An error occurred while trying to retrieve the books")

# Retrieve a specific book by name
@bookapirouter.get("/{name}")
async def getbook(name:str):
    try:
        book = books_serialize(collection_name.find_one({"name":name}))
        return {"data":book}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")

# Create a new book
@bookapirouter.post("/")
async def create_book(book: Book):
    try:
        _id = collection_name.insert_one(dict(book))
        return {"data": books_serialize(collection_name.find({"_id": _id.inserted_id})), "status_code": 201}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=500, detail="An error occurred while trying to create the book")

# Update an existing book
@bookapirouter.put("/{id}")
async def update_book(id: str, book: Book):
    try:
        collection_name.find_one_and_update({"_id": ObjectId(id)}, {
            "$set": dict(book)
        })
        return {"data": books_serialize(collection_name.find({"_id": ObjectId(id)})), "status_code": 200}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@bookapirouter.delete("/{id}")
async def delete_book(id:str):
    try:
        collection_name.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": "ok", "status_code": 204}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")