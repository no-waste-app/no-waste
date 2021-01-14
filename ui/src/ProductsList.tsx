import { List } from "antd";

class Props {
  data: string[] = [];
}

export const ProductsList = ({ data }: Props): JSX.Element => {
  return (
    <List
      style={{ minWidth: "25%", marginTop: "20px" }}
      itemLayout="horizontal"
      dataSource={data}
      bordered={true}
      renderItem={(item) => <List.Item>{item}</List.Item>}
    />
  );
};
