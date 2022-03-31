const express = require('express');
const cors = require('cors')
const app = express();
const PORT = 8080;

let RGB = [0, 0, 0];

app.use(cors({origin: "*"}));

app.use(express.json());

app.post('/rgb', (req, res) => {
    RGB = req.body;
    console.log(RGB.RGB);
    res.status(200).send({
        RGB: RGB.RGB
    })
    });

app.get('/rgb', (req, res) => {
    res.status(200).send({
        RGB: RGB.RGB
    })
});

app.listen(PORT, () => {console.log('http://localhost:8080')});