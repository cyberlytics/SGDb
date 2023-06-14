<script lang="ts">
  import { Router, Route } from 'svelte-routing';
  import Home from "./routes/Home.svelte";
</script>

<body>
  <Router>
    <Route path="/"><Home /></Route>
  </Router>
</body>
