<script>
    export let group = []
    export let color;
    export let data = [];
</script>
<!--Options for platform-filter.
The color of the box depends on the content in the listobject.
It serves to differentiate between the filters and the tags-->
<div class='left'>
    <!--List contains items and the color of the Maintext and Box changes-->
    {#if group.length > 0}
        <h2 style="color:{color}">Platform</h2>
        <div class='filter_container' style="border-color:{color}">
            <!--a new checkbox is created for each value in the platform list-->
            {#each data as platform}
                <label class="border-zinc-900 text-sm text-gray-900">
                    <input type=checkbox value={platform} bind:group>
                    {platform}<br />
                </label>
            {/each}
        </div>
    {/if}
    <!--List is empty and the color changes to the beginning status-->
    {#if group.length === 0}
        <h2 style="color:rgb(30, 29, 29)">Platform</h2>
                <div class='filter_container' style="border-color:#ccc">
                    {#each data as platform}
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