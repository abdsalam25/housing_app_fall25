from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

app = FastAPI()

model = joblib.load("model.joblib")

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    Partner: str
    Dependents: str
    PhoneService: str

@app.get("/")
def home():
    return {"message": "Churn Prediction API is Live on Cloud!"}

@app.post("/predict")
def predict(data: CustomerData):
    df = pd.DataFrame([data.dict()])
    
    pred = model.predict(df)[0]
    
    result = "Churn" if pred == 1 else "No Churn"
    return {"prediction": int(pred), "label": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)