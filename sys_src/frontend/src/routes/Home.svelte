<script lang="ts">
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";

  import Graph from "../lib/Graph.svelte";
  import Navbar from '../lib/Navbar.svelte';

  const handleNodeClick= async (event: CustomEvent<string>) => {
    navigate(`/game/${event.detail}`);
  }

  onMount(async () => {
    const data = await fetch("http://localhost:8000/")
    const json = await data.json();
    console.log(json);
  });
</script>

<Navbar />
<main id="graph-container">
    <Graph on:nodeclick={handleNodeClick} />
</main>