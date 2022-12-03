<script lang="ts">
  import Sigma from 'sigma';
  import { afterUpdate, createEventDispatcher, onDestroy, onMount } from 'svelte';
  import { buildGraph } from "./graph.ts";
  import FA2Layout from "graphology-layout-forceatlas2/worker";
  import forceAtlas2 from "graphology-layout-forceatlas2";

  import type { SigmaNodeEventPayload } from "sigma/sigma";
  import type Graph from "graphology";
  import type State from "./types/Graph";

  export let searchQuery = "";

  let container: HTMLElement;
  let sigma: Sigma | undefined;
  let fa2Layout: FA2Layout | undefined;

  let graph: Graph;
  const state: State = { searchQuery: "" };
  const dispatch = createEventDispatcher();

  onMount(async () => {
    graph = await buildGraph();

    sigma = new Sigma(graph, container, {
      allowInvalidContainer: true,
      defaultNodeColor: "#a3a3a3",
      renderEdgeLabels: true,
      nodeReducer(node, data) {
        const res = { ...data };
        if (state.hoveredNode == node) {
            res.color = "#95060F";
        }
        if (state.hoveredNodeNeighbors && !state.hoveredNodeNeighbors.has(node) && state.hoveredNode !== node) {
          res.label = "";
          res.color = "#f6f6f6";
        }
        if (state.selectedNode === node) {
          res.highlighted = true;
        }
        return res;
      },
      edgeReducer(edge, data) {
        const res = { ...data };
        if (state.hoveredNode && !graph.hasExtremity(edge, state.hoveredNode)) {
          res.hidden = true;
        }
        return res;
      },
    });

    // bind graph interactions
    sigma.on("clickNode", handleNodeClick);
    sigma.on("enterNode", handleNodeEnter);
    sigma.on("leaveNode", handleNodeLeave);
  });

  const setHoveredNode = (node?: string) => {
    if (node) {
      state.hoveredNode = node;
      state.hoveredNodeNeighbors = new Set(graph.neighbors(node));
    } else {
      state.hoveredNode = undefined;
      state.hoveredNodeNeighbors = undefined;
    }

    // refresh rendering
    sigma.refresh();
  }

  const handleNodeEnter = ({ node }: SigmaNodeEventPayload) => {
    setHoveredNode(node);
    sigma.refresh();
  };

  const handleNodeLeave = () => {
    setHoveredNode(undefined);
    sigma.refresh();
  };

  const handleNodeClick = async ({ node }: SigmaNodeEventPayload) => {
    dispatch("nodeclick", node);
  };

  afterUpdate(() => {
    if (sigma) {
      sigma.refresh();
      if (fa2Layout) {
        fa2Layout.kill();
      }
      const sensibleSettings = forceAtlas2.inferSettings(graph);
      fa2Layout = new FA2Layout(graph, {
        settings: sensibleSettings,
      });
      fa2Layout.start();
    }
  });

  onDestroy(async () => {
    if (fa2Layout) {
      fa2Layout.kill();
      fa2Layout = undefined;
    }
    if (sigma) {
      sigma.kill();
      sigma = undefined;
    }
  });
</script>

<div bind:this={container} class="container" id="sigma-container"/>

<style>
  #sigma-container {
    width: 100%;
    height: 860px;
  }
</style>
