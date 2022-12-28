<script>
    export let group = [];
    export let date = undefined;
    export let color;
    
    //removes the num-tag from the frontend and the list. reset the num-inputs in Date.svlete
    const removeNum = () => date = undefined;

    //removes the tag of the given list-component in frontend and list. 
    function removeTag(tag){
        group = group.filter(i => i !== tag);
    }

</script>
<!--create a new num-tag with given color-->
{#if date!=undefined}
    <span class="input-tag" style="background-color:{color}">{date}</span>
    <button type="button" style="color:{color}" class="remove-tag" on:click={removeNum}>&times;</button>
{/if}
<!--create a new list-tag with given color-->
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