
from fastapi import FastAPI
from main import addItemHere, read_all_items_here
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/addItem")
def read_item(url: str):
     return addItemHere(url)

@app.get("/allItems")
def read_all_items():
     return read_all_items_here()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)