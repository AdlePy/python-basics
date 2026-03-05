from fastapi import FastAPI, Query
from typing import Annotated
from items import router as items_router
from users.views import router as user_router


app = FastAPI()
app.include_router(items_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/hello")
async def hello(name: Annotated[str, Query(min_length=3)]):
    return {"message": f"Hello, {name}"}


@app.get("/add")
async def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}
