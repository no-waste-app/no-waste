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
const Recipes = readJSON<RecipesSchema>("./data/recipes.json");

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
  res.json(await Recipes);
});

app.listen(port, () => {
  console.log(`No-Waste mock listening at http://localhost:${port}`);
});
