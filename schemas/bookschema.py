def book_serialize(Book)->dict:
    return {
        "id": str(Book["_id"]),
        "name": Book["name"],
        "description": Book["description"],
        "publishing_date": Book["publishing_date"],
    }
def books_serialize(Books)->list:
    return [book_serialize(Book) for Book in Books]