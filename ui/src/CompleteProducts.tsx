import React, { useState } from "react";
import { SelectProps } from "antd/es/select";
import { AutoComplete, Input } from "antd";
import { useTranslation } from "react-i18next";
import { Api, Product } from "./api/nowaste";

interface Props {
  onSelect: (value: string) => void;
}

export const CompleteProducts: React.FC<Props> = ({ onSelect }: Props) => {
  const { t } = useTranslation();

  const [options, setOptions] = useState<
    SelectProps<Record<string, unknown>>["options"]
  >([]);

  const handleSearch = async (value: string) => {
    setOptions(value ? await searchResult(value) : []);
  };

  return (
    <AutoComplete
      dropdownMatchSelectWidth={252}
      style={{ width: 350 }}
      options={options}
      onSelect={onSelect}
      onSearch={handleSearch}
    >
      <Input.Search
        size="large"
        placeholder={t("completeProducts.whatDoYouHaveInYourFridge")}
        enterButton
      />
    </AutoComplete>
  );
};

const searchResult = async (query: string) => {
  const nwClient = new Api();
  const res = await nwClient.api.productsList({ q: query });

  return res.data.map((item: Product) => {
    return {
      value: item.name,
      label: <div role={"result"}>{item.name}</div>,
    };
  });
};
