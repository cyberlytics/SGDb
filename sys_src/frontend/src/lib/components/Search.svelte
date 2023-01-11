<script lang="ts">
  import { searchQuery, searchText, isSearchDisabled, isSearchSuggestionVisible } from '$stores/search';
  import SearchSuggestions from '$components/SearchSuggestions.svelte';

  export let search = "";

  const handleSearch = () => {
    // set query for graph search
    searchQuery.set(search);
    // clear search input
    search = "";
    // hide search suggestions
    isSearchSuggestionVisible.set(false);
  };

  const handleSuggestion = async (event: CustomEvent<string>) => {
    // write selected game suggestion into search input
    search = event.detail;
    // execute the search
    handleSearch();
  };

  $: isSearchDisabled.set(search.length == 0);
  $: isSearchSuggestionVisible.set(search.length != 0);
</script>

<div class="w-full">
  <label for="search-input"
         class="mb-2 text-sm font-medium text-gray-900 sr-only">Search</label>
  <div class="relative">
    <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
      <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor"
           viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
      </svg>
    </div>
    <!-- Search input -->
    <input bind:value={search}
           on:input={() => searchText.set(search)}
           type="search"
           id="search-input"
           data-testid="search-input"
           class:rounded-lg={$isSearchDisabled}
           class="block p-4 pl-10 w-full border border-zinc-900 text-sm text-gray-900 rounded-t-lg focus:outline-none"
           placeholder="Suche nach Videospielen..."
           required
    >
    <!-- Search button -->
    <button
            disabled={$isSearchDisabled}
            class:cursor-not-allowed="{$isSearchDisabled}"
            on:click={handleSearch}
            class="text-white absolute right-2.5 bottom-2.5 bg-primary focus:outline-none font-medium rounded-lg text-sm px-4 py-2 disabled:opacity-25"
    >
      Suche
    </button>
    <!-- Search suggestions -->
    {#if $isSearchSuggestionVisible}
    <SearchSuggestions on:suggestclick={handleSuggestion}/>
    {/if}
  </div>
</div>