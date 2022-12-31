from fastapi import FastAPI
from db_wrapper import detailpage_content, search_query, get_root_graph
from db_filter import combine_Filter
import json
from filter_lists import get_data

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse

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

    return root


@app.post("/")
def startpage(filter_requests: dict):
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

    return(root)


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
    # if there is one result, redirect to detail-page of the search-result
    if len(searched_game) == 1:
        # search in the game object for the title of the game
        for k in range(len(searched_game[0])):
            if str(searched_game[0][k]["predicate"]["value"]).find("title") != -1:
                searched_game = searched_game[0][k]["object"]["value"]
                break
        # redirect with title of the game
        return RedirectResponse(url=f"/detail/{searched_game}", status_code=303)
    # if there are more search-results, return all
    else:
        return json.dumps(searched_game)


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