import express from "express";
import fs from "fs";

const app = express();
const port = 8080;

const readJSON = async <T>(filename: string): Promise<T> => {
  const data = await fs.readFileSync(filename);
  return JSON.parse(data.toString());
};

interface RecipesSchema {
  title: string;
  imgUrl: string;
  description: string;
  ingredients: string[];
}

const Products = readJSON<string[]>("./data/products.json");
const Recipes = readJSON<RecipesSchema[]>("./data/recipes.json");

app.get("/api/products", async (req, res) => {
  if (!("q" in req.query)) {
    res.status(400);
    res.send("Missing query string");
    return;
  }

  const phrases = req.query["q"] as string;

  const products = (await Products).filter((value: string) =>
    value.toLowerCase().startsWith(phrases)
  );

  res.json(products);
});

app.get("/api/recipes", async (req, res) => {
  let recipes = await Recipes;

  if ("q" in req.query) {
    let query: string[];
    if (typeof req.query["q"] === "string") {
      query = (req.query["q"] as string).split(";");
    } else if (req.query["q"] instanceof Array) {
      query = req.query["q"] as string[];
    } else {
      res.status(400);
      res.send("Unsupported query format");
      return;
    }

    recipes = recipes.filter((recipe: RecipesSchema) =>
      recipe.ingredients
        .flatMap((ingredient: string) =>
          query.map((q: string) => ingredient.includes(q))
        )
        .reduce((acc: boolean, val: boolean) => acc || val)
    );
  }

  res.json(recipes);
});

app.listen(port, () => {
  console.log(`No-Waste mock listening at http://localhost:${port}`);
});
