<script lang="ts">
  import { searchQuery } from "$stores/search";

  let search = "";

  $: isSearchDisabled = search.length == 0;
  $: console.log($searchQuery)
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
    <input bind:value={search} type="search" id="search-input"
           class="block p-4 pl-10 w-full border border-zinc-900 text-sm text-gray-900 rounded-lg focus:outline-none"
           placeholder="Suche nach Videospielen..." required
    >
    <button
            disabled={isSearchDisabled}
            class:cursor-not-allowed="{isSearchDisabled}"
            on:click={() => searchQuery.set(search)}
            class="text-white absolute right-2.5 bottom-2.5 bg-primary focus:outline-none font-medium rounded-lg text-sm px-4 py-2 disabled:opacity-25"
    >
      Suche
    </button>
  </div>
</div>