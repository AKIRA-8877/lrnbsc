import streamlit as st
import joblib

model = joblib.load("models/puppy_model.joblib")

weight = st.number_input("Enter puppy weight (kg)")
if weight:
    age = model.predict([[weight]])[0]
    st.success(f"Estimated Age: {age:.1f} weeks 🐶")