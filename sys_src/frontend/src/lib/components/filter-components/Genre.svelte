<script>
    import Tags from "./Tags.svelte";
    let group = []
    let genres = ['Indie', 'Classic', 'Action', 'Music', 'Puzzle']
</script>
<div class="left">
    <h2>Genre</h2>
    <div class='filter_container'>

        {#each genres as genre}
            <label class="border-zinc-900 text-sm text-gray-900">
                <input type=checkbox value={genre} bind:group>
                {genre} <br />
            </label>
        {/each}
    </div>
</div>
{#if group!=undefined}
    {#each group as tag}
        <Tags bind:tag={tag} bind:group={group}/>
    {/each}
{/if}
<style>
    .left{
        float: left;
    }
    h2{
        color: rgb(30, 29, 29);
    }
    .filter_container{
        margin-right: 1em;
        border: 2px solid #ccc;
        width: 180px;
        height: 98px;
        overflow-y: scroll;
        text-align: left;
    }
</style>