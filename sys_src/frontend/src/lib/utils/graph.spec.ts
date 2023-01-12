import { buildGraph } from './graph';

describe("graph", () => {
  it("builds an empty graph", async () => {
    const graph = await buildGraph([], []);
    expect(graph).toBeDefined();
  });
});