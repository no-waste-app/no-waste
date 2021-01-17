import {
  render,
  screen,
  waitForElementToBeRemoved,
} from "@testing-library/react";
import { Recipes } from "./Recipes";
import { MemoryRouter } from "react-router-dom";
import { server } from "./mocks/server";
import { rest } from "msw";

describe("Recipes", () => {
  it("should display received recipes", async () => {
    render(
      <MemoryRouter>
        <Recipes />
      </MemoryRouter>
    );

    await waitForElementToBeRemoved(() => screen.getByText(/^Loading/));

    expect(screen.getByText(/Spaghetti/i)).toBeInTheDocument();
    expect(screen.getByText(/Grilled chicken/i)).toBeInTheDocument();
  });

  it("should display filtered recipes", async () => {
    render(
      <MemoryRouter
        initialEntries={[{ pathname: "/recipes", search: "?q=tomatoes" }]}
      >
        <Recipes />
      </MemoryRouter>
    );

    await waitForElementToBeRemoved(() => screen.getByText(/^Loading/));

    expect(screen.getByText(/Spaghetti/i)).toBeInTheDocument();
    expect(screen.queryByText(/Grilled chicken/i)).toBeNull();
  });

  it("should display human readable error message in case of server error", async () => {
    const testErrorMessage = "THIS IS A TEST FAILURE";
    server.use(
      rest.get("/api/recipes", async (req, res, ctx) => {
        return res(ctx.status(500), ctx.json({ message: testErrorMessage }));
      })
    );

    render(
      <MemoryRouter>
        <Recipes />
      </MemoryRouter>
    );

    await waitForElementToBeRemoved(() => screen.getByText(/^Loading/));
    const linkElement = screen.getByText(/try again/i);
    expect(linkElement).toBeInTheDocument();
  });
});
