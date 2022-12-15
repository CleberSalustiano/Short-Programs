import express from "express";

const app = express();

import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

app.use(express.json());

app.get("/", async (request, response) => {
  const users = await prisma.user.findMany({include: {posts: true}});
  return response.send(users);
})

app.post('/', async (request, response) => {
  const {email, name} = request.body;

  const user = await prisma.user.create({data: {email, name}});

  return response.send(user);
})

app.put("/", async (request, response) => {
  
})

app.listen(3333, () => {
  console.log("Listen port " + 3333)
})