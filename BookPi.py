from fastapi import FastAPI
from routes.bookroute import bookapirouter
from fastapi import FastAPI

description="Unlock a world of knowledge with our powerful book retrieval API. Discover a vast collection of books from various genres."

app = FastAPI(
    title="BookPi",
    version="v1.0",
    description=description,
    redoc_url=None
)

app.include_router(bookapirouter)