import streamlit as st
import requests
import os

st.title("Customer Churn Predictor (Advanced Model)")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen?", ["No", "Yes"])
    partner = st.selectbox("Has Partner?", ["No", "Yes"])
    dependents = st.selectbox("Has Dependents?", ["No", "Yes"])

with col2:
    phone = st.selectbox("Phone Service?", ["Yes", "No"])
    tenure = st.number_input("Tenure (Months)", min_value=0, value=12)
    charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)

if st.button("Predict"):
    payload = {
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "tenure": int(tenure),
        "MonthlyCharges": float(charges),
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone
    }
    
    url = "http://api:8000/predict"
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            
            if result['label'] == "Churn":
                st.error(f"⚠️ Prediction: {result['label']}")
            else:
                st.success(f"✅ Prediction: {result['label']}")
        else:
            st.error(f"API Error: {response.text}")
    except Exception as e:
        st.error(f"Connection Error: {e}")