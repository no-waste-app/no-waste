import { rest } from "msw";
import { RecipesModel } from "../models";

const recipes: RecipesModel[] = [
  {
    title: "Spaghetti",
    ingredients: ["tomatoes", "pasta"],
    description: "",
    imgUrl: "",
  },
  {
    title: "Grilled chicken",
    ingredients: ["chicken", "olive"],
    description: "",
    imgUrl: "",
  },
];

export const handlers = [
  rest.get<RecipesModel>("/api/products?q=mil", (req, res, ctx) => {
    return res(ctx.json([["milk"] as string[]]));
  }),
  rest.get<RecipesModel>("/api/recipes", (req, res, ctx) => {
    const query = req.url.searchParams.getAll("q");
    let response = recipes;

    if (query.length > 0) {
      response = recipes.filter((recipe: RecipesModel) =>
        recipe.ingredients
          .flatMap((ingredient: string) =>
            query.map((q: string) => ingredient.includes(q))
          )
          .reduce((acc: boolean, val: boolean) => acc || val)
      );
    }

    return res(ctx.json(response));
  }),
];
