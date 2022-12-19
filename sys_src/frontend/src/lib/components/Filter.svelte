<script>
    import Creator from "./filter-components/Creator.svelte";
    import Genre from "./filter-components/Genre.svelte";
    import Platform from "./filter-components/Platform.svelte";
    import Date from "./filter-components/Date.svelte";
    import Tags from "./filter-components/Tags.svelte"

    let creator;
    let num;
    let genre;
    let platform;

    let genre_color= 'rgb(90, 73, 157)';
    let creator_color ='rgb(66, 153, 63)';
    let platform_color ='rgb(73, 122, 157)';
    let date_color ='rgb(176, 55, 55)';

    //passes set filters to the backend with post-method
    async function postObj () {
		const res = await fetch('https://httpbin.org/post', {
			method: 'POST',
			body: JSON.stringify({creator,genre,platform,num})
		})
		
		await res.json()
	}
</script>
<div class="filter_box" on:change={postObj}>
    <div class="position">
        <Genre bind:group={genre} bind:color={genre_color}/>  
        <Platform bind:group={platform} bind:color={platform_color}/> 
        <Creator bind:group={creator} bind:color={creator_color}/>    
        <Date bind:num={num} bind:color={date_color}/>
    </div>
    <div class="tags">
        <Tags bind:group={creator} bind:color={creator_color}/>
        <Tags bind:group={genre} bind:color={genre_color}/>
        <Tags bind:group={platform} bind:color={platform_color}/>
        <Tags bind:num={num} bind:color={date_color}/>
    </div>

</div>
<style>
    .position{
        position: relative;
    }
    .filter_box {
		width: 69em;
        height: 11em;
        border: 1px solid rgb(47, 47, 47);
        border-radius: 7px;
        box-shadow: 2px 2px 8px rgba(145, 65, 65, 0.1);
        padding: 2em;
        margin-left: 1.5em;
        margin-top: 5em;
        
	}
    p{
        color: rgb(30, 29, 29); 
    }
</style>