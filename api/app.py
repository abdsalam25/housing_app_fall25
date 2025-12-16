from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

app = FastAPI()

model = joblib.load("model.joblib")

class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    Partner: str
    Dependents: str
    PhoneService: str

@app.get("/")
def home():
    return {"message": "Churn Prediction API is Live!"}

@app.post("/predict")
def predict(data: Customer):
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)[0]
    return {"prediction": int(pred), "label": "Churn" if pred == 1 else "No Churn"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)