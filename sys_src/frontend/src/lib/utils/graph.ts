import Graph from "graphology";
import random from "graphology-layout/random";


export const buildStartPageGraph = async (json: Object) => {
  const nodes = [];
  const edges = [];
  // root node
  nodes.push({ id: 0, label: "Erscheinungsjahr", size: 20 });
  // iterate over all release years in json object
  for (let [key, values] of Object.entries(json['data'])) {
    const name = key.toString()
    nodes.push({ id: name, label: name, size: 10 });
    edges.push({ source: 0, target: name });
    // @ts-ignore
    values.forEach((gameTitle: String) => {
      nodes.push({ id: gameTitle, label: gameTitle, size: 5 });
      edges.push({ source: name, target: gameTitle });
    });
  }
  // build graph with nodes and edges
  return buildGraph(nodes, edges);
}

export const buildGraph = async (nodes, edges): Promise<Graph> => {
  // create graph
  const g = new Graph();
  // add nodes to graph object
  for (const node of nodes) {
    if (!g.hasNode(node.id)){
      g.addNode(node.id, { size: node.size, label: node.label })
    }
  }
  // add edges to graph object
  for (const edge of edges) {
    if (g.hasNode(edge.source) && g.hasNode(edge.target)) {
      if (!g.hasEdge(edge.source, edge.target)) {
        g.addEdge(edge.source, edge.target, {
          type: "arrow", size: 3, weight: 1
        });
      }
    }
  }
  // init random graph layout
  random.assign(g);
  return g;
}