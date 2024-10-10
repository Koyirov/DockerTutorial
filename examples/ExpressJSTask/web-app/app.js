'use strict';

const express = require('express')

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express()

app.get('/', function (req, res) {
    res.send('<h1>Hello World from Express.js in Docker</h1>')
})

app.listen(PORT, HOST, () => {
    console.log(`Running on http://${HOST}:${PORT}`);
});