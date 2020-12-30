import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders no waste title", () => {
  render(<App />);
  const linkElement = screen.getByText(/no waste/i);
  expect(linkElement).toBeInTheDocument();
});
