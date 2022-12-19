<script lang="ts">
  import { navigate } from "svelte-routing";
  import { buildStartPageGraph } from "$utils/graph";

  import Graph from "$components/Graph.svelte";
  import Navbar from '$components/Navbar.svelte';

  const handleNodeClick= async (event: CustomEvent<string>) => {
      navigate(`/game/${event.detail}`);
  };

  const fetchGraph = async (): Promise<Graph> => {
      const data = await fetch("http://localhost:8000/")
      const json = await data.json();
      return await buildStartPageGraph(json);
  };
</script>


<main id="graph-container">
    <Navbar />
    {#await fetchGraph()}
        <p class="text-black text-2xl p-8">Loading Graph...</p>
    {:then graph}
        <Graph on:nodeclick={handleNodeClick} {graph} />
    {:catch error}
        <p class="text-primary">{error.message}</p>
    {/await}
</main>