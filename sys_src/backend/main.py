from fastapi import FastAPI
from db_wrapper import detailpage_content, query_all
from typing import Optional

# for debugging purpose
import uvicorn

app = FastAPI()
graph = query_all()

@app.get("/")
def startpage():
    return{"message": "Startpage"}

# search request
# load list-page with games with similiar names to searched game
@app.get("/search")
def search(search: str = None):
    # search in the database for the requested game
    #search_result = game_search(graph, search)
    return{"message": search}

# detailpage
# todo: if only one item is returend from search(), then it should be instantly linked to the detail page
@app.get("/detail/{game}")
def detailpage(game: str):
    return{"message": detailpage_content(graph, game)}


# debugging purpose
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8810)