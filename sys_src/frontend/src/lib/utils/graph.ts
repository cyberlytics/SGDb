import Graph from "graphology";
import circular from "graphology-layout/random";

const nodes = [
  { id: "John", label: "John" },
  { id: "Mary", label: "Mary" },
  { id: "Thomas", label: "Thomas" },
  { id: "Hannah", label: "Hannah" },
];

const edges = [
  { source: "John", target: "Mary" },
  { source: "John", target: "Thomas" },
  { source: "John", target: "Hannah" },
  { source: "Hannah", target: "Thomas" },
  { source: "Hannah", target: "Mary" },
];

export async function buildGraph(): Promise<Graph> {
  console.log("building graph");

  const g = new Graph();

  for (const node of nodes) {
    g.addNode(node.id, { size: 20, label: node.label });
  }

  for (const edge of edges) {
    g.addEdge(edge.source, edge.target, {
      type: "arrow", label: "knows", size: 3, weight: 1
    });
  }

  circular.assign(g);
  return g;
}