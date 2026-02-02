# Topic of the Day: Building a CRUD API (FastAPI)
#
# Explanation: CRUD is the lifecycle of data. Yesterday we did GET (Read). Today we add PUT (Update) and DELETE.
#
# Path Parameters: .../items/{item_id} targeting a specific item.

from fastapi import FastAPI, HTTPException

app = FastAPI()

# Temporary database (Dictionary)
items = {1: "Laptop", 2: "Mouse"}

# 1. READ (Get all)
@app.get("/items")
def get_items():
    return items

# 2. CREATE (Add new)
@app.post("/items/{item_id}")
def create_item(item_id: int, name: str):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = name
    return {"message": "Created", "item": name}

# 3. UPDATE (Change existing)
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = name
    return {"message": "Updated", "item": name}

# 4. DELETE (Remove)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Deleted"}