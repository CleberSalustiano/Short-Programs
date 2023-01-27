const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

io.on('connection', socket => {
  socket.on('send message', message => {
    io.emit('received message', message);
  });
});

server.listen(3000);
