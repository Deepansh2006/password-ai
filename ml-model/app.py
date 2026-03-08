from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

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


@app.route("/")
def home():
    return jsonify({"message": "Password Strength API is running"})


@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():

    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.get_json()

    if not data or "password" not in data:
        return jsonify({"error": "Password is required"}), 400

    password = data["password"]

    features = extract_features(password)
    prediction = model.predict(features)[0]

    return jsonify({
        "password": password,
        "strength": str(prediction)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)