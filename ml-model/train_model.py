import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("../dataset/password_dataset.csv")

# Feature extraction function
def extract_features(password):

    length = len(password)

    has_upper = int(bool(re.search(r'[A-Z]', password)))
    has_lower = int(bool(re.search(r'[a-z]', password)))
    has_digit = int(bool(re.search(r'[0-9]', password)))
    has_special = int(bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)))

    digit_count = len(re.findall(r'\d', password))

    return [length, has_upper, has_lower, has_digit, has_special, digit_count]


# Create feature matrix
X = np.array([extract_features(p) for p in data['password']])

# Labels
y = data['strength']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "password_model.pkl")

print("Model saved successfully")