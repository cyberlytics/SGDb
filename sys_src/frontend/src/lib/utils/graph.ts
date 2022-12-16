import Graph from "graphology";
import random from "graphology-layout/random";


export async function buildGraph(json): Promise<Graph> {
  console.log("building graph");

  const g = new Graph();

  g.addNode("Erscheinungsjahr", { size: 20, label: "Erscheinungsjahr" });

  const nodes = [];
  const edges = [];
  for (let [key, values] of Object.entries(json)) {
    const name = key.toString()
    nodes.push({ id: name, label: name });
    edges.push({ source: "Erscheinungsjahr", target: name });
    // @ts-ignore
    values.forEach((gameTitle: String) => {
      nodes.push({ id: gameTitle, label: gameTitle });
      edges.push({ source: name, target: gameTitle });
    });
  }

  for (const node of nodes) {
    if (!g.hasNode(node.id)){
      g.addNode(node.id, { size: 10, label: node.label })
    }
  }

  for (const edge of edges) {
    if (g.hasNode(edge.source) && g.hasNode(edge.target)) {
      if (!g.hasEdge(edge.source, edge.target)) {
        g.addEdge(edge.source, edge.target, {
          type: "arrow", size: 3, weight: 1
        });
      }
    }
  }

  console.log(
      "Graph has " + g.order + " nodes and " + g.size + " edges."
  )

  random.assign(g);
  return g;
}