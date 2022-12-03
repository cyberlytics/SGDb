from SPARQLWrapper import SPARQLWrapper, JSON
from typing import Optional

# for debugging purpose
import uvicorn

# ontotext url should be here
graphdb_url = 'http://localhost:7200/repositories/movies'

# db object initialize
sparql = SPARQLWrapper(graphdb_url)
sparql.setReturnFormat(JSON)

# todo: Query for whole Graph
sparql.setQuery("""
    PREFIX imdb: <http://academy.ontotext.com/imdb/>
    PREFIX schema: <http://schema.org/>

    SELECT * { 
        ?movie a imdb:ColorMovie ;
           schema:name ?movieName ;
           schema:commentCount ?commentCount .
    }   
    ORDER BY DESC(?commentCount)
    LIMIT 5
""")

# catch any errors if query goes wrong
try:
    ret = sparql.queryAndConvert()
    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)

# todo: query for search; search after game-name
    # param1: sparql object, which is generated in this file
    # param2: game-name from main.py
    # return json with possible games

# games is only as long as we dont have data in our database
games = [
{"name": "cs:go", "preis": 0, "genre": "Shooter"},
{"name": "dota", "preis": 20, "genre": "Moba"},
{"name": "dota2", "preis": 30, "genre": "Moba"},
{"name": "need for speed", "preis": 50, "genre": "Rennspiel"},
]

# refine this function to search in database, as soon as the database is accesable
# should be case-insensitiv query if possible
def search_query(search: str = None):
    if search is not "":
        search_results = []
        for item in games:
            # if there is an item with exact the search term, it will give only that item back
            if item["name"] == search and not search in item["name"]:
                return item
            # if more items in the database include the search term, it will give all the results back
            elif search in item["name"]:
                search_results.append(item)
        if len(search_results) == 0:
            return {"no game": "not found any match"}
        else:
            return search_results
    else:
        return {"no game": "please enter some game"}

    

# todo: query for filter-options; load new graph with filter(s) activated
    # param1: sparql object, which is generated in this file
    # param2: filter-options from main.py
    # return json with new graph