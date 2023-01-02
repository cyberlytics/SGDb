<script>
    import Creator from "./filter-components/Creator.svelte";
    import Genre from "./filter-components/Genre.svelte";
    import Platform from "./filter-components/Platform.svelte";
    import Date from "./filter-components/Date.svelte";
    import Tags from "./filter-components/Tags.svelte";

    export let filter;

    let creator;
    let date;
    let genre;
    let platform;

    let genre_color= 'rgb(90, 73, 157)';
    let creator_color ='rgb(66, 153, 63)';
    let platform_color ='rgb(73, 122, 157)';
    let date_color ='rgb(176, 55, 55)';

    //convert to json-string for post request
    const handleChange = () => {
        filter = "";
        filter = JSON.stringify({creator,platform,genre,date});
    }

</script>
<!--Modal contains filter options and set filteritem tags-->
<div class="filter_box" on:change={handleChange}>
    <div class="position">
        <!--Creates new filteroptions, returns checked items as values in a list 
        and passes color-variables for style-->
        <Genre bind:group={genre} bind:color={genre_color} />  
        <Platform bind:group={platform} bind:color={platform_color}/>
        <Creator bind:group={creator} bind:color={creator_color}/>    
        <Date bind:date={date} bind:color={date_color}/>
    </div>
    <div class="tags">

         <!--Creates new tags as checked, passes meantfor colors and values-->
        <Tags bind:creator={creator} bind:color={creator_color}/>
        <Tags bind:group={genre} bind:color={genre_color}/>
        <Tags bind:group={platform} bind:color={platform_color}/>
        <Tags bind:date={date} bind:color={date_color}/>
    </div>
</div>
<style>
    .position{
        position: relative;
    }
    .filter_box {
		width: 69em;
        margin-top: 2em;
        margin-bottom: 2em;
	}
    p{
        color: rgb(30, 29, 29); 
    }
    .tags {
        margin-left: 47em;
        width: 20em;
        height: 7em;
        overflow-y: auto;
    }
</style>