<script>
    import Tags from "./Tags.svelte";
    let num;
    
</script>
<div class="left">
	<h2>Year</h2>
	<label class='border-zinc-900 text-sm text-gray-900'>
		<input type=number bind:value={num} min=1970 max=2022>
		<input type=range bind:value={num} min=1970 max=2022>
	</label>
</div>

{#if num!=undefined}
    <Tags bind:tag={num} />
{/if}

<style>
    p{
        color: rgb(30, 29, 29); 
    }
    .left{
        float: left;
    }
    h2 {
        color: rgb(30, 29, 29);
    }
</style>