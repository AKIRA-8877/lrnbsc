# utils.py
import pandas as pd

def should_retrain(log_file="logs/predictions.csv", threshold=5):
    try:
        df = pd.read_csv(log_file, header=None)
        return len(df) >= threshold
    except FileNotFoundError:
        return False