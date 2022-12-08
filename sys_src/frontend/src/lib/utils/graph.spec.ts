import { buildGraph } from './graph';

describe("graph", () => {
  it("builds a graph", async () => {
    const graph = await buildGraph();
    expect(graph).toBeDefined();
  });
});