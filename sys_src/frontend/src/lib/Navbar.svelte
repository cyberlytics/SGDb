<script lang="ts">
  let searchQuery = "";

  $: isSearchDisabled = searchQuery.length == 0;
  $: isFilterDisabled = isSearchDisabled;
</script>

<nav class="bg-white px-2 sm:px-4 py-2">
  <div class="container flex flex-row items-center justify-between mx-auto">
    <div class="text-xl select-none font-semibold whitespace-nowrap text-primary mr-8">
      SGDb
    </div>
    <div class="w-full">
      <form>
        <label for="default-search"
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
          <input bind:value={searchQuery} type="search" id="default-search"
                 class="block p-4 pl-10 w-full border border-zinc-900 text-sm text-gray-900 rounded-lg focus:outline-none"
                 placeholder="Suche nach Videospielen..." required
          >
          <button
                  type="submit"
                  disabled={isSearchDisabled}
                  class:cursor-not-allowed="{isFilterDisabled}"
                  class="text-white absolute right-2.5 bottom-2.5 bg-primary focus:outline-none font-medium rounded-lg text-sm px-4 py-2 disabled:opacity-25"
          >
            Suche
          </button>
        </div>
      </form>
    </div>
    <button
            disabled={isFilterDisabled}
            class:cursor-not-allowed="{isFilterDisabled}"
            class="text-primary rounded-lg focus:outline-none font-medium text-sm px-4 py-2 ml-2 hover:bg-primary/25 disabled:text-zinc-400 disabled:hover:bg-zinc-400/25"
    >
      Filter
    </button>
  </div>
</nav>