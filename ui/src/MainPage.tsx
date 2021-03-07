import { useState } from "react";
import { CompleteProducts } from "./CompleteProducts";
import { ProductsList } from "./ProductsList";
import { Button, Typography } from "antd";
import { SearchOutlined } from "@ant-design/icons";
import { useHistory } from "react-router-dom";
import { useTranslation } from "react-i18next";

const { Title } = Typography;

export function MainPage(): JSX.Element {
  const { t } = useTranslation();

  const history = useHistory();
  const [products, setProducts] = useState([] as string[]);

  const onSelect = (value: string) => {
    setProducts([...products, value]);
  };

  const query =
    products.length > 0 ? "?" + products.map((p) => `q=${p}`).join("&") : "";

  return (
    <>
      <Title style={{ textAlign: "center" }}>No Waste</Title>
      <CompleteProducts onSelect={onSelect} />
      {products.length > 0 && (
        <>
          <ProductsList data={products} />
          <Button
            className={"button-search-recipes"}
            type="primary"
            icon={<SearchOutlined />}
            onClick={() => history.replace("/recipes" + query)}
          >
            {t("mainPage.searchButton")}
          </Button>
        </>
      )}
    </>
  );
}
