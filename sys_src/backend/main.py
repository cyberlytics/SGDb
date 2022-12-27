from fastapi import FastAPI
from db_wrapper import detailpage_content, search_query, get_root_graph, query_the_subject
from db_filter import combine_Filter
import json
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


# returns a root-graph in dependency to the release-date of a game
@app.get("/")
def startpage():
    root_graph = get_root_graph()
    root = {'data': {}, 'filters': {}}
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

    return root


@app.post("/")
def startpage(filter_requests: dict):
    # only keep dict keys with values inside
    for set_filter in filter_requests:
        if set_filter == "":
            del filter_requests[set_filter]

    filter_graph_iri = combine_Filter(filter_requests)

    filtered_games = []
    for i in filter_graph_iri:
        filtered_iri = query_the_subject(i)
        filtered_iri = filtered_iri["results"]["bindings"]
        filtered_games.append(filtered_iri)

    game_info = {}
    for filtered_game in filtered_games:
        game_date = ""
        game_list = []
        for k in range(len(filtered_game)):
            if str(filtered_game[k]["predicate"]["value"]).find("title") != -1:
                game_list.append(filtered_game[k]["object"]["value"])
            if str(filtered_game[k]["predicate"]["value"]).find("Date") != -1:
                game_date = filtered_game[k]["object"]["value"][0:4]
        if game_date:
            if game_date not in game_info:
                game_info[game_date] = game_list
            else:
                game_info[game_date].extend(game_list)
    return game_info

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
    json_game_list = {"direct_matches": game_list}

    if not game_list:
        return JSONResponse(
            status_code=404,
            content={"message": "Game not found"},
        )

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