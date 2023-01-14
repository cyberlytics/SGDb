from fastapi import FastAPI
from db_wrapper import search_query, get_root_graph, query_game_details
from db_filter import combine_Filter, recommendations
from filter_lists import get_data
from utils import escaping_string

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


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
                content={"message": "invalid date input, only int allowed"},
            )
    if "rating_num" in filter_requests:
        if not isinstance(filter_requests["rating_num"], int):
                return JSONResponse(
                status_code=404,
                content={"message": "invalid rating_num input, only int allowed"},
            )

    root = {'data': {}, 'filters': {}}
    root_graph = combine_Filter(filter_requests)

    if None in root_graph:
            return JSONResponse(
            status_code=404,
            content={"message": "no matching game with the used filter"},
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
    # escape string
    search = escaping_string(search)
    # search in the database for the requested game
    searched_game = search_query(search)
    game_list = []
    for i in range(len(searched_game["results"]["bindings"])):
        game_list.append(searched_game["results"]["bindings"][i]["title"]["value"])
    json_game_list = {"matches": game_list}

    if not game_list:
        return JSONResponse(
            status_code=404,
            content={"message": "searched game not found"},
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
    # escape string
    game = escaping_string(game)
    query_result = query_game_details(game)

    if len(query_result['results']['bindings']) == 0:
        return JSONResponse(
            status_code=404,
            content={"message": "no game for detailpage found"},
        )

    content = query_result['results']['bindings'][0]

    recommends = recommendations(content)
    content["recommends"] = recommends
    return content

