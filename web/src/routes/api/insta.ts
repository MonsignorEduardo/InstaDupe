import { Handlers } from "$fresh/server.ts";

export const handler: Handlers = {
  async POST(req, _ctx) {
    return new Response(JSON.stringify({ message: "Hello World" }));
  },
};
