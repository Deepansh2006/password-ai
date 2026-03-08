import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [password, setPassword] = useState("");
  const [strength, setStrength] = useState("");

  const checkPassword = async () => {
    try {
      const response = await axios.post("https://password-ai-1.onrender.com/check-password", {
        password: password,
      });

      setStrength(response.data.strength);
    } catch (error) {
      console.error(error);
      setStrength("Error checking password");
    }
  };

  const getStrengthColor = () => {
    if (strength === "Weak") return "red";
    if (strength === "Medium") return "orange";
    if (strength === "Strong") return "green";
    return "black";
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