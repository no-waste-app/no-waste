import React from "react";
import "./App.css";
import { Layout, Menu, Typography } from "antd";
import { CompleteProducts } from "./CompleteProducts";

const { Title } = Typography;
const { Header, Footer, Content } = Layout;

function App(): JSX.Element {
  return (
    <Layout className={"App"}>
      <Header className={"App-header"}>
        <Menu
          className={"App-header-menu"}
          mode="horizontal"
          defaultSelectedKeys={["home"]}
        >
          <Menu.Item key="home">Home</Menu.Item>
          <Menu.Item key="recipes">Recipes</Menu.Item>
          <Menu.Item key="about">About</Menu.Item>
        </Menu>
      </Header>
      <Content className={"App-content"}>
        <Title style={{ textAlign: "center" }}>No Waste</Title>
        <CompleteProducts />
      </Content>
      <Footer className={"App-footer"}>Built by Johny Inc.</Footer>
    </Layout>
  );
}

export default App;
