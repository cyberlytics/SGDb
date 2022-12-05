<script lang="ts">
  import { navigate } from "svelte-routing";

  import Graph from "../lib/Graph.svelte";
  import Navbar from '../lib/Navbar.svelte';

  const handleNodeClick= async (event: CustomEvent<string>) => {
    navigate(`/game/${event.detail}`);
  }
</script>

<Navbar />
<main id="graph-container">
    <Graph on:nodeclick={handleNodeClick} />
</main>