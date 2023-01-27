import React, { useState, useEffect } from 'react';
import socketIOClient from 'socket.io-client';

const Chat = () => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);
  const [socket] = useState(socketIOClient('http://localhost:3000'));

  useEffect(() => {
    socket.on('received message', message => setMessages([...messages, message]));
  }, [messages]);

  const handleSubmit = e => {
    e.preventDefault();
    socket.emit('send message', message);
    setMessage('');
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={e => setMessage(e.target.value)}
        />
        <button type="submit">Enviar</button>
      </form>
      <div>
        {messages.map((message, index) => (
          <div key={index}>{message}</div>
        ))}
      </div>
    </div>
  );
};

export default Chat;