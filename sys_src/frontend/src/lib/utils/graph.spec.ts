import { buildGraph,  buildStartPageGraph} from './graph';

describe("graph", () => {
  it("builds an empty graph", async () => {
    const graph = await buildGraph([], []);
    expect(graph).toBeDefined();
  });
  it("builds startpagegraph", async () => {
    const startpagegraph = await buildStartPageGraph(object);
    expect(startpagegraph).toBeDefined();
  });
});