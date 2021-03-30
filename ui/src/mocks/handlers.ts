import { rest } from "msw";
import { Ingredients, Product, Recipe } from "../api/nowaste";

const recipes: Recipe[] = [
  {
    title: "Spaghetti",
    ingredients: [
      { name: "tomatoes", quantity: "2" },
      { name: "pasta", quantity: "0.5lb" },
    ],
    directions: "Some directions",
    description: "",
    imgUrl: "",
  },
  {
    title: "Grilled chicken",
    ingredients: [
      { name: "chicken", quantity: "1 whole chicken" },
      { name: "olive", quantity: "2 tbps" },
    ],
    directions: "some different directions",
    description: "",
    imgUrl: "",
  },
];

export const handlers = [
  rest.get<Recipe>("/api/products", (req, res, ctx) => {
    const query = req.url.searchParams;
    const q = query.get("q");

    if (q == "mil") {
      return res(ctx.json([{ name: "milk" }] as Product[]));
    }

    return res(ctx.json([] as Product[]));
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
