from fastapi import FastAPI
from db_wrapper import query_all, detailpage_content, search_query, get_root_graph, query_the_subject
from db_filter import combine_Filter
import json
from pydantic import BaseModel
from filter_lists import get_data

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

# for debugging purpose
import uvicorn

app = FastAPI()
graph = query_all()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FilterModel(BaseModel):
    filter_requests: dict

# returns a root-graph in dependency to the release-date of a game
@app.get("/")
def startpage():
    root_graph = get_root_graph(graph)
    root = {'data': {}, 'fiters': {}}
    for year in range(1985,2023):
        title_in_year = []
        for i in range(len(root_graph["results"]["bindings"])):
            year_string = root_graph["results"]["bindings"][i]["year"]["value"]
            if year_string.find(str(year)) != -1:
                title_in_year.append(root_graph["results"]["bindings"][i]["title"]["value"])
        root['data'][year] = title_in_year

    # add filter names to startpage
    filter_data = get_data(graph)
    print(filter_data)
    for data in filter_data:
        root['fiters'].update(data)

    return root

@app.post("/")
def startpage(filter_requests: dict):
    for set_filter in filter_requests:
        if set_filter == "":
            del filter_requests[set_filter]

    filter_graph_iri = combine_Filter(
        graph,
        filter_requests["date"],
        filter_requests["genre"]
    )
    
    filtered_games = []
    for i in filter_graph_iri:
        filtered_iri = query_the_subject(graph, i)
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
@app.get("/search/{search}")
def search(search: str = None):
    # search in the database for the requested game
    # if there is one result, redirect to detail-page of the search-result
    if len(search_query(graph, search)) == 1:
        return RedirectResponse(url=f"/detail/{search}", status_code=303)
    # if there are more search-results, return all
    else:
        return json.dumps(search_query(graph, search))

# search request if there are no search query named
@app.get("/search/")
def search():
    return{"message": "please enter a title for search"}

# detailpage
@app.get("/detail/{game}")
def detailpage(game: str):
    return json.dumps(detailpage_content(graph, game))

'''
# debugging purpose
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8810)
'''