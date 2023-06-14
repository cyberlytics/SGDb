import { buildGraph,  buildStartPageGraph} from './graph';

describe("graph", () => {

  it("builds an empty graph", async () => {
    const graph = await buildGraph([], []);
    expect(graph).toBeDefined();
  });

  const object = {data: {2000:['test1', 'test2'], 2001:['test1', 'test2']}, filter: {}}

  it("builds startpagegraph", async () => {
    const startpagegraph = await buildStartPageGraph(object);
    expect(startpagegraph).toBeDefined();
  });
});