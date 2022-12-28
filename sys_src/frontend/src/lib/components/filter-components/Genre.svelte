<script>
    export let group = [];
    export let color;
    export let data = [];
</script>
<!--Options for genre-filter.
The color of the box depends on the content in the listobject.
It serves to differentiate between the filters and the tags-->
<div class="left">
    {#if group.length > 0}
     <!--List contains items and the color of the Maintext and Box changes-->
        <h2 style="color:{color}">Genre</h2>
        <div class='filter_container' style="color:{color}">
            <!--a new checkbox is created for each value in the genre list-->
            {#each data as genre}
                <label class="border-zinc-900 text-sm text-gray-900">
                    <input type=checkbox value={genre} bind:group>
                    {genre} <br />
                </label>
            {/each}
        </div>
    {/if}
    <!--List is empty and the color changes to the beginning status-->
    {#if group.length === 0}
    <h2 style="color:rgb(30, 29, 29)">Genre</h2>
        <div class='filter_container' style="border-color:#ccc">
            {#each data as genre}
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