// Core
const http = require('http');
const path = require('path');

// Express
const express = require('express');
const cors = require("cors");

// Socket.IO
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: "*"
});

app.use(cors({ origin: "*" }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const menuRouter = require('./apis/menuRouter');
const reviewController = require('./apis/reviewController');

app.use('/images', express.static(path.join(__dirname, 'data/images')));

io.on("connection", (socket) => {
  console.log("Client connected:", socket.id);
});

setInterval(() => {
  io.emit("time", new Date().toLocaleTimeString("en-AU", {timeZone: "Australia/Sydney"}));
}, 1000);

app.use("/menu", menuRouter);
app.use("/review", reviewController);

server.listen(3000, () => {
  console.log("Server started at port 3000...");
});
