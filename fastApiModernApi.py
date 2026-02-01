# Topic of the Day: FastAPI (Modern APIs)
#
# Explanation: On Day 20, we used Flask. FastAPI is the new industry favorite.
# It is faster, automatically generates documentation (Swagger UI), and uses modern Python type hints.
#
# Key Feature: Automatic data validation.
#
# Code: Note: Run pip install fastapi uvicorn first.

from fastapi import FastAPI

app = FastAPI()

# 1. Define a Route with Type Hints
# FastAPI automatically checks if item_id is an integer!
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Super Item"}

# 2. To Run
# Save this file as main.py
# Run in terminal: uvicorn main:app --reload
# Then open browser to: http://127.0.0.1:8000/docs (Auto-generated UI!)