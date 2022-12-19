<script>
    import Tags from "./Tags.svelte";
    export let group = [];
    export let color;
    let creators = ['SasaGames', 'LalaGames', 'MoserGames', 'LoloGames']

</script>
<div class="left">
    {#if group.length > 0}
            <h2 style="color:{color}">Creator</h2>
            <div class='filter_container' style="border-color:{color}">
                {#each creators as creator}
                    <label class="border-zinc-900 text-sm text-gray-900">
                        <input type=checkbox value={creator} bind:group>
                        {creator}<br />
                    </label>
                {/each}
            </div>
    {/if}
    {#if group.length === 0}
        <h2 style="color:rgb(30, 29, 29)">Creator</h2>
                <div class='filter_container' style="border-color:#ccc">
                    {#each creators as creator}
                        <label class="border-zinc-900 text-sm text-gray-900">
                            <input type=checkbox value={creator} bind:group>
                            {creator}<br />
                        </label>
                    {/each}
                </div>
    {/if}

</div>
<style>
    p{
        color: rgb(30, 29, 29);
    }
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