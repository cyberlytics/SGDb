<script>
    import Creator from "./filter-components/Creator.svelte";
    import Genre from "./filter-components/Genre.svelte";
    import Platform from "./filter-components/Platform.svelte";
    import Date from "./filter-components/Date.svelte";
    import Tags from "./filter-components/Tags.svelte";
    import {filterSettings, isApplyDisabled, isInputDisabled} from '$stores/filter.ts';

    export let creator=[];
    export let platform=[];
    export let genre=[];
    let date;

    let genre_color= 'rgb(90, 73, 157)';
    let creator_color ='rgb(66, 153, 63)';
    let platform_color ='rgb(73, 122, 157)';
    let date_color ='rgb(176, 55, 55)';

    //saves filtersettings in filtermodal
    let filter;
    $: filter = JSON.stringify({creator, platform, genre, date});
    $: filterSettings.set(filter);
    $: if(creator.length==0 && platform.length==0 && genre.length==0 && date==undefined){
        filterSettings.set('');
    }

    //disables the apply button, if no filter are set
    $: isApplyDisabled.set($filterSettings == '');

    if($filterSettings!=''){
        let settings = JSON.parse($filterSettings);
        creator= settings.creator;
        platform= settings.platform;
        genre= settings.genre;
        date= settings.date;
    }

    //disables checkbox inputs
    $: if(creator.length + platform.length + genre.length >= 4){
        isInputDisabled.set(true);
    }else {isInputDisabled.set(false)}


</script>
<!--Modal contains filter options and set filteritem tags-->
<div class="filter_box">
    <div class="position" data-testid='inputs'>
        <!--Creates new filteroptions, returns checked items as values in a list 
        and passes color-variables for style-->
        <Genre bind:group={genre} bind:color={genre_color} />  
        <Platform bind:group={platform} bind:color={platform_color}/>
        <Creator bind:group={creator} bind:color={creator_color}/>    
        <Date bind:date={date} bind:color={date_color}/>
    </div>
    <div class="tags" data-testid='tags'>
         <!--Creates new tags as checked, passes meantfor colors and values-->
        <Tags bind:group={creator} bind:color={creator_color}/>
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
    .tags {
        margin-left: 47em;
        width: 20em;
        height: 7em;
        overflow-y: auto;
    }
</style>