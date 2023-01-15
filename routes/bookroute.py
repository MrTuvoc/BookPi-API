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
@bookapirouter.get("/all")
async def show_books():
    try:
        books = books_serialize(collection_name.find())
        return {"data":books}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=500, detail="An error occurred while trying to retrieve the books")

# Retrieve a specific book by name
@bookapirouter.get("/book/{name}")
async def book_by_name(name:str):
    try:
        book = books_serialize(collection_name.find_one({"name":name}))
        return {"data":book}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")

# Add a new book
@bookapirouter.post("/add")
async def add_book(book: Book):
    try:
        _id = collection_name.insert_one(dict(book))
        return {"data": books_serialize(collection_name.find({"_id": _id.inserted_id})), "status_code": 201}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=500, detail="An error occurred while trying to create the book")

# Update an existing book
@bookapirouter.put("/update/{id}")
async def update_book(id: str, book: Book):
    try:
        collection_name.find_one_and_update({"_id": ObjectId(id)}, {
            "$set": dict(book)
        })
        return {"data": books_serialize(collection_name.find({"_id": ObjectId(id)})), "status_code": 200}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@bookapirouter.delete("/delete/{id}")
async def delete_book(id:str):
    try:
        collection_name.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": "ok", "status_code": 204}
    except (PyMongoError, ConnectionFailure):
        raise HTTPException(status_code=404, detail="Book not found")