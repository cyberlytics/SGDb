<script>
    export let date;
    export let color;
</script>
<!--Options for year-date-filter.
The color of the maintext depends on the content in the num-object.
It serves to differentiate between the filters and the tags-->
<div class="left">
    <!--numobject is empty and the color changes to the beginning status-->
    {#if date===undefined}
        <h2 style="color: rgb(30, 29, 29)">Year</h2>     
    {/if}
    <!--numobject has value and the color changes to recognizable color-->
    {#if date > 0}
        <h2 style="color:{color}">Year</h2>
    {/if}
    <!--creates a input with number and a range
        the settings for the max and min values ​​depend on the age of the games-->
    <label class='border-zinc-900 text-sm text-gray-900'>
        <input type=range bind:value={date} min=1980 max=2022 data-testid='date-input'>
    </label>
</div>

<style>
    .left{
        float: left;
    }
</style>