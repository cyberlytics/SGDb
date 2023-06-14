<script>
  import Filter from './Filter.svelte';
  import { isFilterVisible, graphData, isPost, filterSettings, isApplyDisabled } from '$stores/filter.ts';

  const handleClose = () => {
    isFilterVisible.set(false);
  };

  const handleFilterCancel = () => {
    filterSettings.set('');
    isPost.set(false);
    isFilterVisible.set(false);
  };

  //passes set filteritems to backend with post-request
  async function postFilter () {
    isPost.set(true);
    isFilterVisible.set(false);
    if($filterSettings!=''){
      const response = await fetch("http://localhost:8000/", {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: $filterSettings
      });
      graphData.set(response.json());
    }
  }
</script>

<div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
  <!-- Background backdrop -->
  <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

  <div class="fixed inset-0 z-10 overflow-y-auto">
    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
      <!--
        Modal panel, show/hide based on modal state.
      -->
      <div class="relative min-w-max transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
        <div class="absolute top-0 right-0 hidden pt-4 pr-4 sm:block">
          <button
                  on:click={handleClose}
                  type="button"
                  data-testid="close-button"
                  class="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
            <span class="sr-only">Close</span>
            <!-- Heroicon name: outline/x-mark -->
            <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="flex">
          <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
            <!-- Heroicon name: outline/adjustments-horizontal -->
            <svg class="h-6 w-6 text-red-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
            </svg>
          </div>
          <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
            <h3 class="text-lg font-medium leading-6 text-gray-900" id="modal-title">Filter</h3>
            <Filter />
          </div>
        </div>
        <div class="mt-5 sm:mt-4 sm:flex sm:flex-row-reverse">
          <button
                  disabled={$isApplyDisabled}
                  class:cursor-not-allowed="{$isApplyDisabled}"
                  on:click={postFilter}
                  type="button"
                  data-testid="apply-button"
                  class="inline-flex w-full justify-center rounded-md border border-transparent bg-primary px-4 py-2 text-base font-medium text-white shadow-sm disabled:opacity-25 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm">
            Anwenden
          </button>
          <button
                  on:click={handleFilterCancel}
                  type="button"
                  data-testid="cancel-button"
                  class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:w-auto sm:text-sm">
            Abbrechen
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
