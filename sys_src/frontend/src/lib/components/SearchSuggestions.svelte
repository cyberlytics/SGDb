<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { searchText } from '$stores/search';

  const dispatch = createEventDispatcher();

  const dispatchSelectedEvent = async (text: string) => {
    dispatch("suggestclick", text);
  };

  const formatData = (data) => {
    if(!data || !data.hasOwnProperty('matches')) return [];
    return data['matches'];
  };

  export const fetchSuggestions = async (search: string) => {
    const data = await fetch("http://localhost:8000/search/" + search);
    const response = await data.json();
    return formatData(response);
  };

</script>

<ul class="absolute z-10 max-h-60 w-full overflow-auto rounded-b-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none divide-y" id="options" role="listbox">
  {#await fetchSuggestions($searchText) then matches}
    {#each matches as match}
      <li
              id="option-0"
              role="option"
              tabindex="-1"
              on:click={() => dispatchSelectedEvent(match)}
              class="flex items-start select-none py-2 pl-3 pr-9 text-gray-900 hover:bg-gray-100"
      >
        <span class="block truncate pl-8">{match}</span>
      </li>
    {/each}
  {/await}
</ul>