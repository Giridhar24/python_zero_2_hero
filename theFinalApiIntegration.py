# Topic of the Day: The Final API (Integration)
#
# Explanation: This is a Production-Ready endpoint.
#
# It accepts data, validates it, runs a Machine Learning prediction, and logs the result to a (simulated) database.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random # Simulating our ML model

app = FastAPI()

# 1. Data Validation Model (Pydantic)
class HouseFeatures(BaseModel):
    rooms: int
    location_score: float

# 2. The Endpoint
@app.post("/predict_price")
def predict_house_price(features: HouseFeatures):
    # Step A: Validation
    if features.rooms < 1:
        raise HTTPException(status_code=400, detail="House must have at least 1 room")

    # Step B: The "Data Science" Model
    # (In real life, this would be: model.predict([[features.rooms, ...]]))
    base_price = 100000
    predicted_price = base_price + (features.rooms * 20000) + (features.location_score * 5000)

    # Step C: The "Database" Log
    print(f"LOG: Saving prediction ${predicted_price} to DB...")

    # Step D: Response
    return {
        "status": "success",
        "input": features,
        "prediction": predicted_price
    }