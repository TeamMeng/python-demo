from typing import Optional
from fastapi import FastAPI, Header
from pydantic.main import BaseModel

app = FastAPI()


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/greet/")
async def greet(name: Optional[str] = "User", age: int = 0):
    return {"message": f"Hello I'm {name}, age: {age}"}


@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {"title": book_data.title, "author": book_data.author}


@app.get("/get_headers", status_code=201)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content_type"] = content_type
    request_headers["User_agent"] = user_agent
    request_headers["host"] = host

    return request_headers


def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
