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
    const linkElement = screen.getByText(/Some recipe/i);
    expect(linkElement).toBeInTheDocument();

    // await userEvent.type(screen.getByLabelText(/username/i), "johnUser");
    //
    // userEvent.click(screen.getByRole("button", { name: /submit/i }));
    //
    // expect(
    //   await screen.findByText("f79e82e8-c34a-4dc7-a49e-9fadc0979fda")
    // ).toBeInTheDocument();
    // expect(await screen.findByText("John")).toBeInTheDocument();
    // expect(await screen.findByText("Maverick")).toBeInTheDocument();
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
