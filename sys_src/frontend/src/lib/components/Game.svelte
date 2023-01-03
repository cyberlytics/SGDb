<script lang="ts">
  import { selectedGame, isDetailsVisible } from "$stores/game";
  const fetchGameDetails = async () => {
    const data = await fetch("http://localhost:8000/detail/" + $selectedGame.replace(' ', '_'));
    return await data.json();
  };
  
</script>

<svelte:head>
  <title>Game Information</title>
  {#await fetchGameDetails() then details}
  <meta name="twitter:card" content= {details.description} />
  <meta name="twitter:title" content= {$selectedGame}/>
  <meta name="twitter:description" content= {details.description} />
  <meta name="twitter:image" content= {details.image}/>
  {/await}
</svelte:head>

{#await fetchGameDetails() then details}
  <main>
    <div class="relative z-10" aria-labelledby="slide-over-title" role="dialog" aria-modal="true">

      <div class="fixed inset-0 overflow-hidden bg-gray-200 bg-opacity-60">
        <div class="absolute inset-0 overflow-hidden">
          <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10 sm:pl-16">
    
            <div class="pointer-events-auto n w-screen max-w-2xl">
              <div class="flex h-full flex-col overflow-y-scroll bg-white shadow-xl">
                <div class="px-4 py-6 sm:px-6">
                  <div class="flex items-start justify-between">
    
                    <h2 class="text-lg font-medium text-gray-900" id="slide-over-title">Game Information</h2>
    
                    <div class="ml-3 flex h-7 items-center">
                      <button on:click={() => isDetailsVisible.set(false)} type="button" class="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:ring-2 focus:ring-indigo-500">
                        <span class="sr-only">Close panel</span>
                        <!-- Heroicon name: outline/x-mark -->
                        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
                <!-- Main -->
                <div class="divide-y divide-gray-200">
                  <div class="pb-6">
                    <div class="h-24 bg-primary sm:h-20 lg:h-28"></div>
                    <div class="lg:-mt-15 -mt-12 flow-root px-4 sm:-mt-8 sm:flex sm:items-end sm:px-6">
                      <div>
                        <div class="-m-1 flex">
                          <div class="inline-flex overflow-hidden rounded-lg border-4 border-white">
                            <img class="h-24 w-24 flex-shrink-0 sm:h-40 sm:w-40 lg:h-48 lg:w-48" src={details.image.value} alt="">
                          </div>
                        </div>
                      </div>
                      <div class="mt-6 sm:ml-6 sm:flex-1">
                        <div>
                          <div class="flex items-center">
                            <h3 class="text-xl font-bold text-gray-900 sm:text-2xl">{$selectedGame}</h3>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="px-4 py-5 sm:px-0 sm:py-0">
                    <dl class="space-y-8 sm:space-y-0 sm:divide-y sm:divide-gray-200">
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48">Description</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6">
                          <p>{details.description.value}</p>
                        </dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48">Creator</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6">{details.creatorName.value}</dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48">Platform</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6">{details.gamePlatformName.value}</dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48">Genre</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6">{details.genreName.value}</dd>
                      </div>
                          <div class="sm:flex sm:px-6 sm:py-5">
                        <dt class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48">Rating</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6">{details.ratingValue.value}</dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48">Release Date</dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6">
                          <time datetime="{details.releaseDate.value}">{details.releaseDate.value}</time>
                        </dd>
                      </div>
                    </dl>
                  </div>
                </div>
                <!-- Recom if exist in Backend-->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
  <footer>
    <p>Team Rot</p>
  </footer>
{/await}