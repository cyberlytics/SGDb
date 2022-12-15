from fastapi import FastAPI
from db_wrapper import query_all, detailpage_content, search_query, get_root_graph
import json

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


# returns a root-graph in dependency to the release-date of a game
@app.get("/")
def startpage():
    root_graph = get_root_graph(graph)
    root = {}
    for year in range(1985,2023):
        title_in_year = []
        for i in range(len(root_graph["results"]["bindings"])):
            year_string = root_graph["results"]["bindings"][i]["year"]["value"]
            if year_string.find(str(year)) != -1:
                title_in_year.append(root_graph["results"]["bindings"][i]["title"]["value"])
        root[year] = title_in_year
    return root

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