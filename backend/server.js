const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.post("/check-password", async (req, res) => {
    try {

        const password = req.body.password;

        const response = await axios.post("http://127.0.0.1:5000/predict", {
            password: password
        });

        res.json(response.data);

    } catch (error) {
        console.error(error);
        res.status(500).json({ error: "Something went wrong" });
    }
});

app.listen(3000, () => {
    console.log("Node server running on http://localhost:3000");
});