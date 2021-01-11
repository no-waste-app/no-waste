import { render, screen } from "@testing-library/react";
import { ProductsList } from "./ProductsList";

describe("LoginForm", () => {
  it("should allow a user to log in", async () => {
    render(<ProductsList data={["asc"]} />);

    const linkElement = screen.getByText(/asc/i);
    expect(linkElement).toBeInTheDocument();
  });
});
