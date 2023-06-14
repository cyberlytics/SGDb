<script lang="ts">
  import { selectedGame, isDetailsVisible } from "$stores/game";

  let recommendationsCount = 0;

  const fetchGameDetails = async (game: string) => {
    const data = await fetch(
      "http://localhost:8000/detail/" + game.replace(" ", "_")
    );
    const json = await data.json();
    recommendationsCount = json.recommends.length;
    return json;
  };

  let currentRecommendationIndex = 0;

  const navigateRecommendations = (offset: number) => {
    currentRecommendationIndex += offset;
    if (currentRecommendationIndex < 0) {
      currentRecommendationIndex = 0;
    } else if ( currentRecommendationIndex >= recommendationsCount) {
      currentRecommendationIndex = recommendationsCount - 1;
    }
  }

  $: gameDetails = fetchGameDetails($selectedGame);
</script>

<svelte:head>
  {#await gameDetails then details}
    <meta name="twitter:card" content={details.description.value} />
    <meta name="twitter:title" content={$selectedGame} />
    <meta name="twitter:description" content={details.description.value} />
    <meta name="twitter:image" content={details.image.value} />
  {/await}
</svelte:head>

{#await gameDetails then details}
  <main>
    <div
      class="relative z-10"
      aria-labelledby="slide-over-title"
      role="dialog"
      aria-modal="true"
    >
      <div class="fixed inset-0 overflow-hidden bg-gray-200 bg-opacity-60">
        <div class="absolute inset-0 overflow-hidden">
          <div
            class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10 sm:pl-16"
          >
            <div class="pointer-events-auto n w-screen max-w-2xl">
              <div
                class="flex h-full flex-col overflow-y-scroll bg-white shadow-xl"
              >
                <div class="px-4 py-6 sm:px-6">
                  <div class="flex items-start justify-between">
                    <h2
                      class="text-lg font-medium text-gray-900"
                      id="slide-over-title"
                    >
                      Videospiel Details
                    </h2>

                    <div class="ml-3 flex h-7 items-center">
                      <button
                        on:click={() => isDetailsVisible.set(false)}
                        type="button"
                        class="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:ring-2 focus:ring-indigo-500"
                      >
                        <span class="sr-only">Close panel</span>
                        <!-- Heroicon name: outline/x-mark -->
                        <svg
                          class="h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M6 18L18 6M6 6l12 12"
                          />
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
                <!-- Main -->
                <div class="divide-y divide-gray-200">
                  <div class="pb-6">
                    <div class="h-24 bg-primary sm:h-20 lg:h-28" />
                    <div
                      class="lg:-mt-15 -mt-12 flow-root px-4 sm:-mt-8 sm:flex sm:items-end sm:px-6"
                    >
                      <div>
                        <div class="-m-1 flex">
                          <div
                            class="inline-flex overflow-hidden rounded-lg border-4 border-white"
                          >
                            <img
                              class="h-24 w-24 flex-shrink-0 sm:h-40 sm:w-40 lg:h-48 lg:w-48"
                              src={details.image.value}
                              alt=""
                            />
                          </div>
                        </div>
                      </div>
                      <div class="mt-6 sm:ml-6 sm:flex-1">
                        <div>
                          <div class="flex items-center">
                            <h3
                              class="text-xl text-left font-bold text-gray-900 sm:text-2xl"
                            >
                              {$selectedGame}
                            </h3>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="px-4 py-5 sm:px-0 sm:py-0">
                    <dl
                      class="space-y-8 sm:space-y-0 sm:divide-y sm:divide-gray-200"
                    >
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt
                          class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48"
                        >
                          Description
                        </dt>
                        <dd
                          class="mt-1 text-sm text-left text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6"
                        >
                          <p>{details.description.value}</p>
                        </dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt
                          class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48"
                        >
                          Creator
                        </dt>
                        <dd
                          class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6"
                        >
                          {details.creatorNames.value}
                        </dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt
                          class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48"
                        >
                          Platform
                        </dt>
                        <dd
                          class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6"
                        >
                          {details.gamePlatformNames.value}
                        </dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt
                          class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48"
                        >
                          Genre
                        </dt>
                        <dd
                          class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6"
                        >
                          {details.genreNames.value}
                        </dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt
                          class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48"
                        >
                          Rating
                        </dt>
                        <dd
                          class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6"
                        >
                          {details.ratingValue.value}/100
                        </dd>
                      </div>
                      <div class="sm:flex sm:px-6 sm:py-5">
                        <dt
                          class="text-sm font-medium text-gray-500 sm:w-40 sm:flex-shrink-0 lg:w-48"
                        >
                          Release Date
                        </dt>
                        <dd
                          class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0 sm:ml-6"
                        >
                          <time datetime={details.releaseDate.value}
                            >{new Date(
                            details.releaseDate.value
                            ).toLocaleString("de-DE", {
                              month: "long",
                              day: "numeric",
                              year: "numeric",
                            })}</time
                          >
                        </dd>
                      </div>
                    </dl>
                  </div>
                </div>
                {#if details.recommends}
                  <div class="recommendations mt-6">
                    <h3 class="text-lg font-medium text-gray-900">
                      Recommended Games
                    </h3>
                    <div class="flex justify-between mt-3">
                      <button
                        on:click={() => navigateRecommendations(-1)}
                        type="button"
                        class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                      >
                        <span class="sr-only">Previous</span>
                        <!-- Heroicon name: solid/chevron-left -->
                        <svg
                          class="h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M15 19l-7-7 7-7"
                          />
                        </svg>
                      </button>
                      <div class="relative rounded-md shadow-sm">
                        <div
                          class="relative inline-flex align-middle h-full rounded-md overflow-hidden"
                        >
                          {#each details.recommends.slice(currentRecommendationIndex, currentRecommendationIndex + 3) as recommendation}
                            <div
                                    on:click={() => selectedGame.set(recommendation.title.value)}
                              class="relative w-32 h-48 rounded-md overflow-hidden bg-gray-100 bg-opacity-50 mr-2"
                            >
                              <img
                                class="w-full h-full object-cover"
                                src={recommendation.image.value}
                                alt={recommendation.title.value}
                              />
                            </div>
                          {/each}
                        </div>
                      </div>
                      <button
                        on:click={() => navigateRecommendations(1)}
                        type="button"
                        class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                      >
                        <span class="sr-only">Next</span>
                        <!-- Heroicon name: solid/chevron-right -->
                        <svg
                          class="h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M9 5l7 7-7 7"
                          />
                        </svg>
                      </button>
                    </div>
                  </div>
                {/if}
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
