const http = require('http');
console.log("3333333333")
console.log("3333333333")
console.log("3333333333")
console.log("3333333333")
console.log("3333333333")
console.log("3333333333")
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});
console.log("3333333333")
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
