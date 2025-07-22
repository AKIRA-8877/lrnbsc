from flask import Flask, request, render_template_string
import joblib
import os
import csv
from datetime import datetime

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/puppy_model.joblib")

# Simple HTML template for input form and result display
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <title>Puppy Age Predictor</title>
  </head>
  <body>
    <h1>Puppy Age Predictor</h1>
    <form method="post">
      <label for="weight">Enter puppy weight (kg):</label>
      <input type="number" step="any" id="weight" name="weight" required>
      <button type="submit">Predict Age</button>
    </form>
    {% if age is not none %}
      <h2>Estimated Age: {{ age }} weeks</h2>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def predict():
    age = None
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            age = model.predict([[weight]])[0]
            age = round(age, 1)

            # Log prediction
            os.makedirs("logs", exist_ok=True)
            with open("logs/predictions.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), weight, age])
        except Exception as e:
            age = f"Error: {e}"

    return render_template_string(HTML_TEMPLATE, age=age)

if __name__ == "__main__":
    app.run(debug=True)
