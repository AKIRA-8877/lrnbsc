# train.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
df = pd.read_csv("data/puppies.csv")

# Train model
model = LinearRegression()
model.fit(df[['weight']], df['age'])

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/puppy_model.joblib")
print("✅ Model trained and saved.")