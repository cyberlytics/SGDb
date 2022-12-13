<script lang="ts">
  import Search from '$components/Search.svelte';

  $: isFilterDisabled = true;
</script>

<nav class="bg-gradient-to-b from-white to-transparent fixed w-full z-20 px-2 sm:px-4 py-2 pb-4">
  <div class="container flex flex-row items-center justify-between mx-auto">
    <div class="text-2xl select-none font-semibold whitespace-nowrap text-primary mr-8">
      SGDb
    </div>
    <Search />
    <button
            data-testid="filter-button"
            disabled={isFilterDisabled}
            class:cursor-not-allowed="{isFilterDisabled}"
            class="text-primary rounded-lg focus:outline-none font-medium text-sm px-4 py-2 ml-2 hover:bg-primary/25 disabled:text-zinc-400 disabled:hover:bg-zinc-400/25"
    >
      Filter
    </button>
  </div>
</nav>