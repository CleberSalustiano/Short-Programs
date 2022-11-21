require("dotenv").config();
const { sign } = require("jsonwebtoken");
const express = require("express");
const app = express();
const authenticate = require("./middleware/auth");
const port = process.env.PORT || 3333;

app.use(express.json());

// Routes
// localhost:3333/publicacao (GET)
app.post("/login", (request, response) => {
	// fs -> busca arquivos
	const fs = require("fs");

	const { username, senha } = request.body;

	const data = fs.readFileSync("./database/users.json", "utf-8");
	const arrayUsers = JSON.parse(data.toString());

	/*
    const user = arrayUsers.find(
      (user) => {
        if (user.username === username) {
          return user;
        }
      }
	  );   
  */

	const user = arrayUsers.find((user) => user.username === username);
    
	const token = sign({ username }, process.env.JWT_SECRET, {
    expiresIn: process.env.JWT_EXPIRESIN,
  });

	return response.json({user, token});
});

app.get("/post", authenticate, (request, response) => {
  const {username} = request.user;

  const fs = require("fs");
  const data = fs.readFileSync("./database/posts.json", "utf-8");
	const arrayPost = JSON.parse(data.toString());

  return response.json(arrayPost)
})
// middleware
// app.post("/login",(request, response, next) => {}, (request, response) => {})

// // publicar informações
// app.post()

// // deletar informação
// app.delete()

// // alterar informação
// app.put()

app.listen(port, () => {
	console.log("Rodando em " + port);
});
