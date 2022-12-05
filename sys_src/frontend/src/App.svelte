<script lang="ts">
  import { Router, Route } from 'svelte-routing';
  import Game from "./routes/Game.svelte";
  import Home from "./routes/Home.svelte";
</script>

<body>
  <Router>
    <Route path="game/:id" let:params>
      <Game id="{params.id}" />
    </Route>
    <Route path="/"><Home /></Route>
  </Router>
</body>
