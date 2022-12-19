<script>
    import Tags from "./Tags.svelte";
    export let num;
    export let color;
</script>
<div class="left">
    {#if num===undefined}
        <h2 style="color: rgb(30, 29, 29)">Year</h2>     
    {/if}
    {#if num > 0}
        <h2 style="color:{color}">Year</h2>
    {/if}
    <label class='border-zinc-900 text-sm text-gray-900'>
        <input type=number bind:value={num} min=1970 max=2022>
        <input type=range bind:value={num} min=1970 max=2022>
    </label>
</div>

<style>
    p{
        color: rgb(30, 29, 29); 
    }
    .left{
        float: left;
    }
</style>