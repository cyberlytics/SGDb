<script lang="ts">
  import Sigma from 'sigma';
  import Graph from 'graphology';
  import { onMount } from 'svelte';

  let container;

  onMount(() => {
    const graph = new Graph();

    graph.addNode("John", { x: 0, y: 10, size: 20, label: "John", color: "red" });
    graph.addNode("Mary", { x: 10, y: 0, size: 20, label: "Mary", color: "red" });
    graph.addNode("Thomas", { x: 7, y: 9, size: 20, label: "Thomas", color: "red" });
    graph.addNode("Hannah", { x: -7, y: -6, size: 20, label: "Hannah", color: "red" });

    graph.addEdge("John", "Mary", { type: "arrow", label: "loves", size: 2 });
    graph.addEdge("John", "Thomas");
    graph.addEdge("John", "Hannah");
    graph.addEdge("Hannah", "Thomas");
    graph.addEdge("Hannah", "Mary");

    // render graph in container
    const renderer = new Sigma(graph, container, { renderEdgeLabels: true });
  });
</script>

<div bind:this={container} class="container" id="sigma-container"/>

<style>
  #sigma-container {
    width: 550px;
    height: 450px;
  }
</style>
