from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def home():
    return {"message": "Helloooooooooooooo, FastAPPPPPPPPPPPPPPPPPPPPPPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
