from flask import Flask, request, jsonify
import joblib
import re
import os

app = Flask(__name__)

# Load trained model
model = joblib.load("password_model.pkl")


def extract_features(password):

    length = len(password)

    has_upper = int(bool(re.search(r'[A-Z]', password)))
    has_lower = int(bool(re.search(r'[a-z]', password)))
    has_digit = int(bool(re.search(r'[0-9]', password)))
    has_special = int(bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)))

    digit_count = len(re.findall(r'\d', password))

    return [[length, has_upper, has_lower, has_digit, has_special, digit_count]]


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    password = data["password"]

    features = extract_features(password)

    prediction = model.predict(features)[0]

    return jsonify({
        "password": password,
        "strength": prediction
    })


# Important for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # Render provides PORT automatically
    app.run(host="0.0.0.0", port=port)