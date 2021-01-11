import { rest } from "msw";
import { RecipesModel } from "../models";
// interface LoginBody {
//   username: string;
// }
// interface LoginResponse {
//   username: string;
//   firstName: string;
// }

export const handlers = [
  // rest.post<LoginBody, LoginResponse>("/login", (req, res, ctx) => {
  //   const { username } = req.body;
  //   return res(
  //     ctx.json({
  //       username,
  //       firstName: "John",
  //     })
  //   );
  // }),
  rest.get<RecipesModel>("/api/products?q=mil", (req, res, ctx) => {
    return res(ctx.json([["milk"] as string[]]));
  }),
  rest.get<RecipesModel>("/api/recipes", (req, res, ctx) => {
    return res(ctx.json([{ title: "Some recipe" } as RecipesModel]));
  }),
];
