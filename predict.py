# predict.py
import joblib
import csv
import os
from datetime import datetime

# Load model
model = joblib.load("models/puppy_model.joblib")

# Get user input
weight = float(input("Enter puppy weight in kg: "))
age = model.predict([[weight]])[0]

print(f"\n🐶 Estimated Age: {age:.1f} weeks")

# Log prediction
os.makedirs("logs", exist_ok=True)
with open("logs/predictions.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([datetime.now(), weight, f"{age:.1f}"])