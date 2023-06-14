<script lang="ts">
  import { buildStartPageGraph } from '$utils/graph';

  import Graph from '$components/Graph.svelte';
  import Navbar from '$components/Navbar.svelte';
  import FilterModal from '$components/FilterModal.svelte';
  import Game from '$components/Game.svelte';
  import { isDetailsVisible, selectedGame } from '$stores/game';
  import { isFilterVisible, filter_data, isPost, graphData } from '$stores/filter.ts';

  const handleNodeClick = async (event: CustomEvent<string>) => {
      // test if node only contains digits
      if (/^\d+$/.test(event.detail)) return;
      selectedGame.set(event.detail);
      isDetailsVisible.set(true);
  };

  const fetchGraph = async (): Promise<Graph> => {
      const data = await fetch("http://localhost:8000/");
      const json = await data.json();
      filter_data.set(json.filters);
      return await buildStartPageGraph(json);
  };
    
</script>

<Navbar />
{#if $isFilterVisible}
    <FilterModal />
{/if}
<main id="graph-container">
    {#if !$isPost}
        {#await fetchGraph()}
            <p class="text-black text-2xl p-8">Lade Graph...</p>
        {:then graph}
            <Graph on:nodeclick={handleNodeClick} {graph} />
        {:catch error}
            <p class="text-primary">{error.message}</p>
        {/await}
    {/if}
    {#if $isPost}
        {#await $graphData then result}   
            {#await buildStartPageGraph(result)}    
            {:then graph} 
                <Graph on:nodeclick={handleNodeClick} {graph} />   
            {/await}
            {:catch error}
                <p class="text-primary">{error.message}</p>
        {/await}
    {/if}
</main>
{#if $isDetailsVisible}
    <Game/>
{/if}