from fastapi import FastAPI
from db_wrapper import search_query
from typing import Optional

# for debugging purpose
import uvicorn

app = FastAPI()

@app.get("/")
def startpage():
    return{"message": "Startpage"}

# search request
# load list-page with games with similiar names to searched game
@app.get("/search")
def search(search: str = None):
    # lowercase search
    search = search.lower()
    # search in the database for the requested game
    search_result = search_query(search)
    return{"message": search_result}

# detailpage
# todo: if only one item is returend from search(), then it should be instantly linked to the detail page
@app.get("/detail/{game}")
def detailpage(game: str):
    return{"message": game}


# debugging purpose
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)