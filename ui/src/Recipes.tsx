import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { Divider } from "antd";
import { Service } from "./service";
import { useTranslation } from "react-i18next";
import { Api, Recipe, RecipesListParams } from "./api/nowaste";

// A custom hook that builds on useLocation to parse
// the query string for you.
function useQuery() {
  return new URLSearchParams(useLocation().search);
}

function RecipeTile(props: { recipe: Recipe }) {
  return (
    <>
      <h4>{props.recipe.title}</h4>
      {props.recipe.imgUrl && (
        <img
          src={props.recipe.imgUrl}
          style={{ width: "100px" }}
          alt={"recipe photo"}
        />
      )}
    </>
  );
}

export function Recipes(): JSX.Element {
  const nwClient = new Api();
  const { t } = useTranslation();
  const urlQuery = useQuery();
  const [recipes, setRecipes] = useState<Service<Recipe[]>>({
    status: "init",
  });

  const recipesQuery = {} as RecipesListParams;

  if (urlQuery.has("q")) {
    recipesQuery.q = urlQuery.getAll("q");
  }

  useEffect(() => {
    async function fetchRecipes() {
      const response = await nwClient.api.recipesList(recipesQuery);
      if (response.ok) {
        setRecipes({ status: "loaded", payload: response.data });
      } else {
        setRecipes({ status: "error", error: await response.text() });
      }
    }

    fetchRecipes().catch((e) => {
      setRecipes({ status: "error", error: e });
    });
  }, []);

  return (
    <>
      {recipes.status == "init" && (
        <div>
          <h3>{t("common.loading")}</h3>
        </div>
      )}
      {recipes.status == "loaded" && recipes.payload.length > 0 ? (
        recipes.payload.map((recipe, idx) => (
          <div key={idx}>
            <RecipeTile recipe={recipe} />
            {idx != recipes.payload.length - 1 && <Divider />}
          </div>
        ))
      ) : (
        <div>
          <h3>{t("common.noData")}</h3>
        </div>
      )}
      {recipes.status == "error" && (
        <div>{t("common.failedToLoadTryLater")}</div>
      )}
    </>
  );
}
