<script>
    export let tag;
    export let group = [];
    function removeTag(tag){
        group = group.filter(i => i !== tag);
    }
</script>

<span class="input-tag">{tag}</span>
<button type="button" class="remove-tag" on:click={() => removeTag(tag)}>&times;</button>


<style>
 .input-tag {
        display: inline-flex;
        line-height: 1.2;
        align-items: center;
        font-size: .875rem;
        background-color: #911a1a;
        color: #f8f4f4;
        border-radius: 7px;
        user-select: none;
        padding: .5rem;
        margin-right: .2rem;
        margin-bottom: .25rem;
        cursor: pointer;
    }
    .remove-tag{
        color: #911a1a;
        font-size: 1.125rem;
        line-height: 1;
    }
</style>