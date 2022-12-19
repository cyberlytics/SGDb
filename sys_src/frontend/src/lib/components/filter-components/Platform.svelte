<script>
    import Tags from "./Tags.svelte";
    export let group = []
    export let color;
    let platforms = ['Xbox', 'Playstation', 'IOS', 'Windows']
</script>
<div class='left'>
    {#if group.length > 0}
        <h2 style="color:{color}">Platform</h2>
        <div class='filter_container' style="border-color:{color}">
            {#each platforms as platform}
                <label class="border-zinc-900 text-sm text-gray-900">
                    <input type=checkbox value={platform} bind:group>
                    {platform}<br />
                </label>
            {/each}
        </div>
    {/if}
    {#if group.length === 0}
        <h2 style="color:rgb(30, 29, 29)">Platform</h2>
                <div class='filter_container' style="border-color:#ccc">
                    {#each platforms as platform}
                        <label class="border-zinc-900 text-sm text-gray-900">
                            <input type=checkbox value={platform} bind:group>
                            {platform}<br />
                        </label>
                    {/each}
                </div>
    {/if}

</div>
<style>
    .left{
        float:left;
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