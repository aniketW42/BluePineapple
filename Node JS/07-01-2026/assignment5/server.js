const express = require("express");
const axios = require("axios");

const server = express(); // seting express app
const PORT = 3000;

server.use(express.json());

server.get("/", (req, res) => {
  res.send("Welcome to Express!"); // respond with "Welcome to Express"!
});

server.post("/data", (req, res) => { // accept JSON data and responce with data received
  console.log(req.body);
  res.send("Data received.");
});

server.get("/users", (req, res) => { // responce with JSON data users
  const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
    { id: 3, name: "Charlie" },
  ];

  res.json(users);
});

server.use((req, res, next) => { // custom middleware to log method and url of every incomming request
  console.log(`${req.method} ${req.url}`);
  next();
});

server.get("/external-posts", async (req, res, next) => { // responce with external data
  try {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/posts"
    );
    res.json(response.data);
  } catch (err) {
    next(err);
  }
});

server.use((req, res) => { // 404 middleware
  res.status(404).send("404 - Route not found");
});

server.use((err, req, res, next) => { // error handling middleware
  console.error(err.stack);
  res.status(500).send("Something went wrong!");
});

server.listen(PORT, () => { // start server at post 3000
  console.log(`Server running on http://localhost:${PORT}`);
});
