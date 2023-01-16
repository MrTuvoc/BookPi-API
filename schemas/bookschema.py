def book_serialize(Book)->dict:
    return {
        "id": str(Book.get("_id")) if '_id' in Book else None,
        "name": Book.get("name"),
        "description": Book.get("description"),
        "publishing_date": Book.get("publishing_date"),
    }

def books_serialize(Books)->list:
    return [book_serialize(Book) for Book in Books if Book is not None]