import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { Divider } from "antd";

interface RecipesModel {
  title: string;
  imgUrl: string;
  description: string;
  ingredients: string[];
}

// A custom hook that builds on useLocation to parse
// the query string for you.
function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export function Recipes(): JSX.Element {
  const query = useQuery();
  const [recipes, setRecipes] = useState([] as RecipesModel[]);

  if (query.get("q")) {
    console.log(query.get("q"));
  }

  useEffect(() => {
    async function fetchRecipes() {
      const response = await fetch(`/api/recipes`);
      const fetchedData = await response.json();
      console.log(fetchedData);
      setRecipes(fetchedData);
    }
    fetchRecipes().then();
  }, []);

  if (recipes.length == 0) {
    return (
      <div>
        <h3>No data</h3>
      </div>
    );
  }

  return (
    <>
      {recipes.map((recipe, idx) => (
        <div key={idx}>
          <h4>{recipe.title}</h4>
          <img
            src={recipe.imgUrl}
            style={{ width: "100px" }}
            alt={"recipe photo"}
          />
          {idx != recipes.length - 1 && <Divider />}
        </div>
      ))}
    </>
  );
}
