<script>
    import Creator from "./filter-components/Creator.svelte";
    import Genre from "./filter-components/Genre.svelte";
    import Platform from "./filter-components/Platform.svelte";
    import Date from "./filter-components/Date.svelte";

</script>
<div class="filter_box">
    <div class="position">
        <Genre />  
        <Platform />   
        <Creator />    
        <Date />
    </div>
</div>

<style>
    .position{
        position: relative;
    }
    .filter_box {
		width: 69em;
        height: 11em;
        border: 1px solid #000;
        border-radius: 7px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        padding: 2em;
        margin-left: 1.5em;
        margin-top: 5em;
        
	}
    p{
        color: rgb(30, 29, 29); 
    }
</style>