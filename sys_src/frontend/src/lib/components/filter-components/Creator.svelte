<script>
    import Tags from "./Tags.svelte";
    let group = [];
    let creators = ['SasaGames', 'LalaGames', 'MoserGames', 'LoloGames']
</script>
<div class="left">
    <h2>Creator</h2>
    <div class='filter_container'>
        {#each creators as creator}
            <label class="border-zinc-900 text-sm text-gray-900">
                <input type=checkbox value={creator} bind:group>
                {creator}<br />
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
    h2 {
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