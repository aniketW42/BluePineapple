const http = require('http')
const {getMessage} = require('./helper')

// printing message using external module
console.log(getMessage())

const server = http.createServer((req, res) => {

    // sending responce
    res.end("Welcome to Node.js!")
})

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
})


