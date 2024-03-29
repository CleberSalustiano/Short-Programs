import { Request, Response } from "express";
import { prismaClient } from "../database/prismaClient";

export class CreateProductWithExistCategory {
	async handle(request: Request, response: Response) {
		const { name, bar_code, price, id_category } = request.body;

		const product = await prismaClient.producttCategory.create({
			data: {
				product: {
					create: {
						name,
						bar_code,
						price,
					},
				},
				category: {
					connect: {
						id: id_category,
					},
				},
			},
		});

		return response.json(product);
	}
}
