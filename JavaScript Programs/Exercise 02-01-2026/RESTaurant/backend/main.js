// Express
const express = require('express');
const cors = require("cors");
const path = require('path');

const app = express();
app.use(cors({origin: "http://127.0.0.1:5500"}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.listen(3000);

const timeRouter = require('./apis/get_time');

const menuRouter = require('./apis/menuRouter');

const reviewController = require('./apis/reviewController');

app.use('/images', express.static(path.join(__dirname, 'data/images')));
app.use("/get-time", timeRouter);
app.use("/menu", menuRouter);
app.use("/review", reviewController);
