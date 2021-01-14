import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { CompleteProducts } from "./CompleteProducts";

describe("Search product", () => {
  it("should allow a user to log in", async () => {
    render(
      <CompleteProducts
        onSelect={function () {
          undefined;
        }}
      />
    );

    await userEvent.type(
      screen.getByPlaceholderText(/What do you have in you fridge?/i),
      "mil"
    );

    userEvent.click(screen.getByRole("button"));

    const result = await screen.findAllByText("milk");
    expect(
      result.find((value) => value.getAttribute("role") === "result")
    ).toBeInTheDocument();
  });
});
