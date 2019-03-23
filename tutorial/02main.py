from fastapi import FastAPI

app = FastAPI()

#Receives HTTP requests in the paths / and /items/{item_id}.
#Both paths take GET operations (also known as HTTP methods).
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
