import { rest } from "msw";
import { Ingredients, Product, Recipe } from "../api/nowaste";

const recipes: Recipe[] = [
  {
    title: "Spaghetti",
    ingredients: [{ name: "tomatoes" }, { name: "pasta" }],
    description: "",
    imgUrl: "",
  },
  {
    title: "Grilled chicken",
    ingredients: [{ name: "chicken" }, { name: "olive" }],
    description: "",
    imgUrl: "",
  },
];

export const handlers = [
  rest.get<Recipe>("/api/products?q=mil", (req, res, ctx) => {
    return res(ctx.json([{ name: "milk" }] as Product[]));
  }),
  rest.get<Recipe>("/api/recipes", (req, res, ctx) => {
    const query = req.url.searchParams.getAll("q");
    let response = recipes;

    if (query.length > 0) {
      response = recipes.filter((recipe: Recipe) => {
        return recipe.ingredients
          ?.flatMap((ingredient: Ingredients) =>
            query.map((q: string) => (ingredient.name || "").includes(q))
          )
          .reduce((accumulator: boolean, val: boolean) => accumulator || val);
      });
    }

    return res(ctx.json(response));
  }),
];
