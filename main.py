from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/greet/{name}")
async def greet(name: str, age: int):
    return {"message": f"Hello I'm {name}, age: {age}"}
