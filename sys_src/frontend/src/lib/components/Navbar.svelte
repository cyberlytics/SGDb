<script lang="ts">
  import Search from '$components/Search.svelte';  
  import { isFilterVisible } from '$stores/filter';

  export const handleClick = () => {
    isFilterVisible.set(true);
  };
</script>

<nav class="bg-white w-full z-20 px-2 sm:px-4 py-2 pb-4">
  <div class="container flex flex-row items-center justify-between mx-auto">
    <div class="text-2xl select-none font-semibold whitespace-nowrap text-primary mr-8">
      <a href="/">SGDb</a>
    </div>
    <Search />
    <button
            data-testid="filter-button"
            on:click={handleClick}
            class="text-primary rounded-lg focus:outline-none font-medium text-sm px-4 py-2 ml-2 hover:bg-primary/25 disabled:text-zinc-400 disabled:hover:bg-zinc-400/25"
    >
      Filter
    </button>
  </div>
</nav>
