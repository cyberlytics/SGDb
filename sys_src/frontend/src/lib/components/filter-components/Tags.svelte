<script>
    export let group = undefined;
    export let creator = undefined;
    export let date = undefined;
    export let color;
    
    //removes the num-tag from the frontend and the list. reset the num-inputs in Date.svlete
    const removeNum = () => date = undefined;
    const removeCreator = () => creator = undefined;

    //removes the tag of the given list-component in frontend and list. 
    function removeTag(tag){
        group = group.filter(i => i !== tag);
    }

</script>
<!--create a new num-tag with given color-->
{#if date!=undefined}
    <span class="input-tag" style="background-color:{color}">{date} 
    <button type="button"  class="remove-tag" on:click={removeNum}>&times;</button></span>
{/if}
{#if creator!=undefined}
    <span class="input-tag" style="background-color:{color}">{creator} 
    <button type="button" class="remove-tag" on:click={removeCreator}>&times;</button></span>
{/if}
<!--create a new list-tag with given color-->
{#if group!=undefined}
    {#each group as tag}
        <span class="input-tag" style="background-color: {color}">{tag} 
            <button type="button" class="remove-tag" on:click={() => removeTag(tag)}>
             &times;
            </button>
        </span>
    {/each}
{/if}

<style>
   p{
        color: black;
    }
 .input-tag {
        display: -webkit-inline-box;
        display: -ms-inline-flexbox;
        display: inline-flex;
        line-height: 1.2;
        -webkit-box-align: center;
            -ms-flex-align: center;
                align-items: center;
        font-size: .875rem;
        color: #f8f4f4;
        border-radius: 7px;
        -webkit-user-select: none;
           -moz-user-select: none;
            -ms-user-select: none;
                user-select: none;
        padding: .5rem;
        margin-right: .2rem;
        margin-bottom: .25rem;
        cursor: pointer;
    }
    .remove-tag{
        color: white;
        margin-left: .5rem;
        font-size: 1.125rem;
        line-height: 1;
    }
</style>