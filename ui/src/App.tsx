import "./App.css";
import { Layout, Menu } from "antd";
import { Route, Switch, Link, BrowserRouter as Router } from "react-router-dom";
import { MainPage } from "./MainPage";
import { Recipes } from "./Recipes";
import { About } from "./About";
import { PageNotFound } from "./PageNotFound";
import { useTranslation } from "react-i18next";

const { Header, Footer, Content } = Layout;

function App(): JSX.Element {
  const { t } = useTranslation();

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
              <Link to={"/"}>{t("navigation.home")}</Link>
            </Menu.Item>
            <Menu.Item key="recipes">
              <Link to={"/recipes"}>{t("navigation.recipes")}</Link>
            </Menu.Item>
            <Menu.Item key="about">
              <Link to={"/about"}>{t("navigation.about")}</Link>
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
              <PageNotFound />
            </Route>
          </Switch>
        </Content>
        <Footer className={"App-footer"}>{t("footer.builtBy")}</Footer>
      </Router>
    </Layout>
  );
}

export default App;
