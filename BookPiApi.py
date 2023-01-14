from fastapi import FastAPI
from routes.bookroute import bookapirouter
app = FastAPI()
app.include_router(bookapirouter)