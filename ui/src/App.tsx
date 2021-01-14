import "./App.css";
import { Layout, Menu } from "antd";
import { Route, Switch, Link, BrowserRouter as Router } from "react-router-dom";
import { MainPage } from "./MainPage";
import { Recipes } from "./Recipes";
import { About } from "./About";

const { Header, Footer, Content } = Layout;

function App(): JSX.Element {
  return (
    <Layout className={"App"}>
      <Router>
        <Header className={"App-header"}>
          <Menu
            className={"App-header-menu"}
            mode="horizontal"
            defaultSelectedKeys={["home"]} //TODO(JN): This is not always true.
          >
            <Menu.Item key="home">
              <Link to={"/"}>Home</Link>
            </Menu.Item>
            <Menu.Item key="recipes">
              <Link to={"/recipes"}>Recipes</Link>
            </Menu.Item>
            <Menu.Item key="about">
              <Link to={"/about"}>About</Link>
            </Menu.Item>
          </Menu>
        </Header>
        <Content className={"App-content"}>
          <Switch>
            <Route exact path={"/"}>
              <MainPage />
            </Route>
            <Route path={"/recipes"}>
              <Recipes />
            </Route>
            <Route path={"/about"}>
              <About />
            </Route>
            <Route path="*">
              <div>404 - Not found</div>
            </Route>
          </Switch>
        </Content>
        <Footer className={"App-footer"}>Built by Johny Inc.</Footer>
      </Router>
    </Layout>
  );
}

export default App;
