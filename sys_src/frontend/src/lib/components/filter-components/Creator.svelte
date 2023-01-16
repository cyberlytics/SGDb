<script>
    import { filter_data, toArray, isInputDisabled} from '$stores/filter.ts';

    export let group = [];
    export let color;
    export let data = toArray($filter_data.creator);
</script>
<!--Options for creator-filter.
The color of the box depends on the content in the listobject.
It serves to differentiate between the filters and the tags-->
<div class="left">
    {#if group.length > 0}
     <!--List contains items and the color of the Maintext and Box changes-->
            <h2 style="color:{color}">Creator</h2>
            <div class='filter_container' style="border-color:{color}">
                <!--a new checkbox is created for each value in the creator list-->
                {#each [...data] as [creator, vals]}
                    <label class="border-zinc-900 text-sm text-gray-900">
                        <input type="checkbox" value={creator} bind:group
                        disabled={$isInputDisabled==true && !group.includes(creator)}>
                        {creator}</label><p>({vals})</p> <br />
                {/each}
            </div>
    {/if}
    <!--List is empty and the color changes to the beginning status-->
    {#if group.length === 0}
        <h2 style="color:rgb(30, 29, 29)">Creator</h2>
                <div class='filter_container' style="border-color:#ccc">
                    {#each [...data] as [creator, vals]}
                        <label class="border-zinc-900 text-sm text-gray-900" data-testid='creator-label'>
                            <input type="checkbox" value={creator} bind:group
                            disabled={$isInputDisabled==true && !group.includes(creator)} data-testid='creator-input'>
                            {creator}</label><p>({vals})</p> <br />
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
        text-align: left;
    }
</style>