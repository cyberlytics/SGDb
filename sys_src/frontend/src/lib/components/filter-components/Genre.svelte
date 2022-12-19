<script>
    import Tags from "./Tags.svelte";
    export let group = []
    export let color;
    let genres = ['Indie', 'Classic', 'Action', 'Music', 'Puzzle']
</script>
<div class="left">
    {#if group.length > 0}
        <h2 style="color:{color}">Genre</h2>
        <div class='filter_container' style="color:{color}">
            {#each genres as genre}
                <label class="border-zinc-900 text-sm text-gray-900">
                    <input type=checkbox value={genre} bind:group>
                    {genre} <br />
                </label>
            {/each}
        </div>
    {/if}
    {#if group.length === 0}
    <h2 style="color:rgb(30, 29, 29)">Genre</h2>
        <div class='filter_container' style="border-color:#ccc">
            {#each genres as genre}
                <label class="border-zinc-900 text-sm text-gray-900">
                    <input type=checkbox value={genre} bind:group>
                    {genre} <br />
                </label>
            {/each}
        </div>
    {/if}
</div>
<style>
    .left{
        float: left;
    }
    .filter_container{
        margin-right: 1em;
        border: 2px solid;
        width: 180px;
        height: 98px;
        overflow-y: scroll;
        text-align: left;
    }
</style>