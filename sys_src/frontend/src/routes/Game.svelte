<script lang="ts">
  //export let id;
  let id = "This Way Madness Lies";
  const fetchGameDetails = async () => {
      const data = await fetch("http://localhost:8000/detail/This%20Way%20Madness%20Lies");
      return await data.json();
  }
</script>

<svelte:head>
  <title>Game Information</title>
  {#await fetchGameDetails() then details}
  <meta name="twitter:card" content= {details.description} />
  <meta name="twitter:title" content= {id}/>
  <meta name="twitter:description" content= {details.description} />
  <meta name="twitter:image" content= {details.image}/>
  {/await}
</svelte:head>

<body>
  {#await fetchGameDetails()}
  <p class="text-black">Loading Graph...</p>
  {:then details}
  <main>
    <h2>{id}</h2>
    <img src={details.image} alt="Game Image">
    <p style="text-align: left;">Game Description:</p>
    <p style="text-align: left;">{details.description}</p>
    <p style="text-align: left;">Platforms: {details.plattform}</p>
    <p style="text-align: left;">Release Date: {details.releaseDate}</p>
    <p style="text-align: left;">Developer: {details.creator}</p>
    <p style="text-align: left;">Publisher: {details.creator}</p>
    <p style="text-align: left;">Genre: {details.genre}</p>
    <p style="text-align: left;">Link to Game:</p>
  </main>
  <footer>
    <p>Team Rot</p>
  </footer>
  {/await}
</body>

<style>
     body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, purple, blue);
      background-size: 400% 400%;
      animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
      0% {
        background-position: 0% 50%;
      }
      50% {
        background-position: 100% 50%;
      }
      100% {
        background-position: 0% 50%;
      }
    }
    h1 {
      text-align: center;
      color: white;
    }
    h2 {
      color: white;
      display: inline-block;
      vertical-align: middle;
    }
    img {
      width: 200px;
      height: 200px;
      display: inline-block;
      vertical-align: middle;
      margin-left: 20px;
      border-radius: 50%;
    }
    p {
      font-size: 16px;
      color: white;
    }
    main {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background-color: rgba(255, 255, 255, 0.7);
      border-radius: 10px;
    }
    footer {
      text-align: center;
      background-color: purple;
      color: white;
      padding: 10px;
    }
</style>