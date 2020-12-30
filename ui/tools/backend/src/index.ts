import express from "express";

const app = express();
const port = 8080;

const Products = [
  "tomatoes",
  "eggs",
  "chicken legs",
  "milk",
  "butter",
  "cooking oil",
  "lettuce",
  "bread",
];

app.get("/api/products", (req, res) => {
  if (!("q" in req.query)) {
    res.status(400);
    res.send("Missing query string");
    return;
  }

  const phrases = req.query["q"] as string;

  const products = Products.filter((value: string) =>
    value.toLowerCase().startsWith(phrases)
  );

  res.json(products);
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
