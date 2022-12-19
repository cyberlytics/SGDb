<script>
    export let group = [];
    export let num = undefined;
    export let color;
    
    const removeNum = () => num = undefined;

    function removeTag(tag){
        group = group.filter(i => i !== tag);
    }

</script>
{#if num!=undefined}
    <span class="input-tag" style="background-color:{color}">{num}</span>
    <button type="button" style="color:{color}" class="remove-tag" on:click={removeNum}>&times;</button>
{/if}
{#if group!=undefined}
    {#each group as tag}
        <span class="input-tag" style="background-color: {color}">{tag}</span>
        <button type="button" class="remove-tag" style="color:{color}" on:click={() => removeTag(tag)}>
            &times;
        </button>
    {/each}
{/if}

<style>
    p{
        color: black;
    }
 .input-tag {
        display: inline-flex;
        line-height: 1.2;
        align-items: center;
        font-size: .875rem;
        color: #f8f4f4;
        border-radius: 7px;
        user-select: none;
        padding: .5rem;
        margin-right: .2rem;
        margin-bottom: .25rem;
        cursor: pointer;
    }
    .remove-tag{
        font-size: 1.125rem;
        line-height: 1;
    }
</style>