import streamlit as st
import requests
import os

st.title("Customer Churn Predictor")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen?", ["No", "Yes"])
tenure = st.number_input("Tenure (Months)", min_value=0, value=12)
charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)

if st.button("Predict"):
    payload = {
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "tenure": int(tenure),
        "MonthlyCharges": float(charges)
    }
    
    url = "http://api:8000/predict"
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['label']}")
        else:
            st.error("Error from API")
    except Exception as e:
        st.error(f"Connection Error: {e}")
        st.info("Ensure Docker is running and the API service is named 'api'.")