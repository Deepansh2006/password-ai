import joblib
import re

# Load trained model
model = joblib.load("password_model.pkl")


# Feature extraction (same as training)
def extract_features(password):

    length = len(password)

    has_upper = int(bool(re.search(r'[A-Z]', password)))
    has_lower = int(bool(re.search(r'[a-z]', password)))
    has_digit = int(bool(re.search(r'[0-9]', password)))
    has_special = int(bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)))

    digit_count = len(re.findall(r'\d', password))

    return [[length, has_upper, has_lower, has_digit, has_special, digit_count]]


# Predict strength
def predict_password_strength(password):

    features = extract_features(password)

    prediction = model.predict(features)

    return prediction[0]


# Test the model
if __name__ == "__main__":

    password = input("Enter password: ")

    result = predict_password_strength(password)

    print("Predicted Strength:", result)