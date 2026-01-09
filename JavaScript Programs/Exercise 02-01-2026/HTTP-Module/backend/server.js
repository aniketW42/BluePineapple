// Http 
const http = require('http');
const { URL } = require('url');

const server = http.createServer((req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);

  if (req.method === 'GET' && parsedUrl.pathname === '/get-time') {
    res.writeHead(200, {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    });

    res.end(JSON.stringify({ time: new Date().toLocaleTimeString() }));
  }
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
});
