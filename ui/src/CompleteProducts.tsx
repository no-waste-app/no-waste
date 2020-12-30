import React, { useState } from "react";
import { SelectProps } from "antd/es/select";
import { AutoComplete, Input } from "antd";

const searchResult = async (query: string) => {
  const result = await fetch(`/api/products?q=${query}`);
  const resultJson = await result.json();

  return (resultJson as string[]).map((item: string) => {
    return {
      value: item,
      label: <div>{item}</div>,
    };
  });
};

export const CompleteProducts: React.FC = () => {
  const [options, setOptions] = useState<
    SelectProps<Record<string, unknown>>["options"]
  >([]);

  const handleSearch = async (value: string) => {
    setOptions(value ? await searchResult(value) : []);
  };

  const onSelect = (value: string) => {
    console.log("onSelect", value);
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
        placeholder="What do you have in you fridge?"
        enterButton
      />
    </AutoComplete>
  );
};
