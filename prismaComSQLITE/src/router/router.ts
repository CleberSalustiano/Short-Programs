import { Router } from "express";
import { prismaClient } from "../database/prismaClient";

const router = Router();

router.post("/", async (request, response) => {
    const {name, type} = request.body

    const product = await prismaClient.product.create({
        data: {name, type}
    })

    return response.json(product);
})

export default router;