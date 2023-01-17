from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from bson import ObjectId
from models.bookmodel import Book
from schemas.bookschema import books_serialize
from config.database import collection_name
from pymongo.errors import PyMongoError, ConnectionFailure

bookapirouter = APIRouter()

# Redirection to documentation page
@bookapirouter.get("/",include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')

# API Status check
@bookapirouter.get("/status",include_in_schema=False)
async def status():
    return {"status":"ok"}

# Retrieve all books
@bookapirouter.get("api/v1/books")
async def show_books():
    try:
        books = books_serialize(collection_name.find())
        return {"data":books}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=500, detail="An error occurred while trying to retrieve the books")

# Retrieve a specific book by name
@bookapirouter.get("api/v1/search/{name}")
async def book_by_name(name: str):
    try:
        book_in_db = collection_name.find_one({"name": {"$regex": name, "$options": "i"}})
        if book_in_db:
            return {"data":books_serialize(book_in_db)}
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")

# Add a new book
@bookapirouter.post("/api/v1/add")
async def add_book(book: Book):
    if all(val is None for val in book.__dict__.values()):
        raise HTTPException(status_code=400, detail="All fields can't be null")
    try:
        _id = collection_name.insert_one(dict(book))
        return {"data": books_serialize(collection_name.find({"_id": _id.inserted_id})), "status_code": 201}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=500, detail="An error occurred while trying to create the book")

# Update a book
@bookapirouter.put("/api1/v1/update/{name}")
async def update_book(name: str, book: Book):
    try:
        book_in_db = collection_name.find_one({"name": {"$regex": name, "$options": "i"}})
        if not book_in_db:
            raise HTTPException(status_code=404, detail="Book not found")
        collection_name.find_one_and_update({"name": {"$regex": name, "$options": "i"}}, {
            "$set": dict(book)
        })
        return {"data": books_serialize(collection_name.find_one({"name": {"$regex": name, "$options": "i"}})), "status_code": 200}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=500, detail="Error while connecting to the database")

# Delete a book
@bookapirouter.delete("/api/v1/delete/{id}")
async def delete_book(id: str):
    try:
        book_in_db = collection_name.find_one({"_id": ObjectId(id)})
        if not book_in_db:
            raise HTTPException(status_code=404, detail="Book not found")
        collection_name.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": "ok", "status_code": 204}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")
