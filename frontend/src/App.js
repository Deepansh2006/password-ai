import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [password, setPassword] = useState("");
  const [strength, setStrength] = useState("");
  const [score, setScore] = useState(0);

  const checkPassword = async () => {
    try {

      const response = await axios.post(
        "https://password-ai-2.onrender.com/predict",
        {
          password: password,
        }
      );

      const result = response.data.strength;
      setStrength(result);

      // Convert strength text → score
      if (result === "Weak") setScore(30);
      else if (result === "Medium") setScore(60);
      else if (result === "Strong") setScore(100);
      else setScore(0);

    } catch (error) {
      console.error(error);
      setStrength("Error checking password");
      setScore(0);
    }
  };

  const getStrengthColor = () => {
    if (strength === "Weak") return "red";
    if (strength === "Medium") return "orange";
    if (strength === "Strong") return "green";
    return "black";
  };

  const getBarColor = () => {
    if (score <= 30) return "#ff4d4d";
    if (score <= 60) return "#ffa500";
    if (score <= 80) return "#9acd32";
    return "#28a745";
  };

  return (
    <div className="main">
      <div className="card">
        <h1>🔐 AI Password Strength Checker</h1>

        <p className="subtitle">
          Check how secure your password is using Machine Learning
        </p>

        <input
          type="password"
          placeholder="Enter your password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={checkPassword}>Check Strength</button>

        {/* Strength Meter */}
        {score > 0 && (
          <div className="meter">
            <div
              className="meter-fill"
              style={{
                width: `${score}%`,
                backgroundColor: getBarColor(),
              }}
            ></div>
          </div>
        )}

        {strength && (
          <div className="result">
            Password Strength:{" "}
            <span style={{ color: getStrengthColor() }}>
              <b>{strength}</b>
            </span>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;