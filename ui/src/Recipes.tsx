import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { Divider } from "antd";
import { RecipesModel } from "./models";
import { Service } from "./service";
import { useTranslation } from "react-i18next";

// A custom hook that builds on useLocation to parse
// the query string for you.
function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export function Recipes(): JSX.Element {
  const { t } = useTranslation();
  const query = useQuery();
  const [recipes, setRecipes] = useState<Service<RecipesModel[]>>({
    status: "init",
  });
  let queryStr = "";

  if (query.getAll("q")) {
    queryStr =
      "?" +
      query
        .getAll("q")
        .map((p) => `q=${p}`)
        .join("&");
  }

  useEffect(() => {
    async function fetchRecipes() {
      const response = await fetch(`/api/recipes${queryStr}`);
      if (response.ok) {
        const fetchedData = await response.json();

        setRecipes({ status: "loaded", payload: fetchedData });
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
            <h4>{recipe.title}</h4>
            <img
              src={recipe.imgUrl}
              style={{ width: "100px" }}
              alt={"recipe photo"}
            />
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
