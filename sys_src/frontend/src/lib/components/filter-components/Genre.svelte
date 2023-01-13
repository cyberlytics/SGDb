<script>
    import { filter_data, toArray, isInputDisabled} from '$stores/filter.ts';
    export let group = [];
    export let color;
    export let data = toArray($filter_data.genre);
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
            {#each [...data] as [genre, vals]}
                <label class="border-zinc-900 text-sm text-gray-900">
                    <input type=checkbox value={genre} bind:group
                    disabled={$isInputDisabled==true && !group.includes(genre)}>
                    {genre} </label><p>({vals})</p> <br />
            {/each}
        </div>
    {/if}
    <!--List is empty and the color changes to the beginning status-->
    {#if group.length === 0}
    <h2 style="color:rgb(30, 29, 29)">Genre</h2>
        <div class='filter_container' style="border-color:#ccc">
            {#each [...data] as [genre, vals]}
                <label class="border-zinc-900 text-sm text-gray-900">
                    <input type=checkbox value={genre} bind:group data-testid='genre-input'
                    disabled={$isInputDisabled==true && !group.includes(genre)}>
                    {genre} </label><p>({vals})</p> <br />
            {/each}
        </div>
    {/if}
</div>
<style>
    p {
        font-size: 14px;
        color:blue;
        float: right;
    }
    label{
        display: inline-block;
        -o-text-overflow:ellipsis;
           text-overflow:ellipsis;
        width: 120px;
        white-space: nowrap;
        overflow: hidden;
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
        overflow-x: scroll;
        text-align: left;
    }
</style>