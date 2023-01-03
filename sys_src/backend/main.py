from fastapi import FastAPI
from db_wrapper import detailpage_content, search_query, get_root_graph
from db_filter import combine_Filter
from filter_lists import get_data

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# for debugging purpose
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = {}

# returns a root-graph in dependency to the release-date of a game
@app.get("/")
def startpage():
    root = {'data': {}, 'filters': {}}
    root_graph = get_root_graph()
    for year in range(1985, 2023):
        title_in_year = []
        for i in range(len(root_graph["results"]["bindings"])):
            year_string = root_graph["results"]["bindings"][i]["year"]["value"]
            if year_string.find(str(year)) != -1:
                title_in_year.append(root_graph["results"]["bindings"][i]["title"]["value"])
        root['data'][year] = title_in_year

    # add filter names to startpage
    filter_data = get_data()
    for data in filter_data:
        root['filters'].update(data)

    global graph 
    graph = root
    return root


@app.post("/")
def filter(filter_requests: dict):
    # check if the filter is only one date and rating
    if "date" in filter_requests:
        if not isinstance(filter_requests["date"], int):
                return JSONResponse(
                status_code=404,
                content={"message": "only Filter one year"},
            )
    if "rating_num" in filter_requests:
        if not isinstance(filter_requests["rating_num"], int):
                return JSONResponse(
                status_code=404,
                content={"message": "only Filter one rating_num"},
            )

    root = {'data': {}, 'filters': {}}
    root_graph = combine_Filter(filter_requests)

    if root_graph is None:
            return JSONResponse(
            status_code=404,
            content={"message": "no matching Game with the Filter"},
        )

    if None in root_graph:
            return JSONResponse(
            status_code=404,
            content={"message": "no matching Game with the Filter"},
        )

    for game in root_graph:
        year = game['date']['value'][:4]  # Extract the year from the "date" field
        title = game['title']['value']  # Extract the game title from the "title" field

        # If the year is not already a key in the dictionary, create a new key-value pair
        # with the year as the key and an empty list as the value
        if year not in root['data']:
          root['data'][year] = []

        # Append the game title to the list of game titles for the current year
        root['data'][year].append(title)

    # add filter names to startpage
    filter_data = get_data()
    for data in filter_data:
        root['filters'].update(data)
    
    global graph 
    graph = root
    return root



# search request
# load list-page with games with similiar names to searched game
@app.get("/search/{search:path}")
def search(search: str = None):
    if search == "":
        return {"message": "please enter a title for search"}
    # remove possible underscore
    search = search.replace("_", " ")
    # search in the database for the requested game
    searched_game = search_query(search)
    game_list = []
    for i in range(len(searched_game["results"]["bindings"])):
        game_list.append(searched_game["results"]["bindings"][i]["title"]["value"])
    json_game_list = {"matches": game_list}

    if not game_list:
        return JSONResponse(
            status_code=404,
            content={"message": "Game not found"},
        )

    games_graph = []
    games_in_graph = []
    games_out_graph = []
    # create a list (games_graph), which contains all games of the graph (no matter if root, or filtered graph)
    for year in graph["data"]:
        for game in graph["data"][year]:
            games_graph.append(game)

    # extract only the games, which are in the graph
    games_in_graph.extend(set(json_game_list["matches"]) & set(games_graph))
    json_game_list.update(match_in_graph = games_in_graph) 

    # extract only the games, which are out of the graph
    games_out_graph.extend(set(json_game_list["matches"]) - set(games_in_graph))
    json_game_list.update(match_out_graph = games_out_graph) 

    return json_game_list

@app.get("/detail/{game}", tags=['Game'])
async def detailpage(game: str):
    """
    Query game details by game name.
    \f
    :param game: Name of the game to query for details.
    """
    content = detailpage_content(game.replace("_", " "))
    if not content:
        return JSONResponse(
            status_code=404,
            content={"message": "Game not found"},
        )
    return content


'''
# debugging purpose
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8810)
'''