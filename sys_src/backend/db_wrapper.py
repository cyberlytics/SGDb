from SPARQLWrapper import SPARQLWrapper, JSON
from typing import Optional

# for debugging purpose
import uvicorn

# Get the url to the graphdb repository
graphdb_url = "http://localhost:7200/repositories/semantic_games"

# db object initialize
sparql = SPARQLWrapper(graphdb_url)
sparql.setReturnFormat(JSON)

# Query for whole Graph
def query_all(sparql_obj):
    """Queries the whole graph and returns it"""
    sparql_obj.setQuery("""
        SELECT * WHERE { 
            ?s ?p ?o .
        }
    """)
    return sparql_obj

# query for search; search after game-name
    # param1: sparql object, which is generated in this file
    # param2: game-name from main.py
    # return json with possible games
def search_game_name(sparql_obj, game_name):
    """Search the Query by the given game name"""
    sparql_obj.setQuery("""
        PREFIX schema: <http://schema.org/>
        SELECT ?s ?p ?o WHERE {{ 
        ?o schema:title "{game_name}" .
        }}
        """.format(game_name=game_name))
    return sparql

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
    
# TODO Sinnvoll Filter nur als String zu übernehmen? Problem bei format, unbekannte Anzahl Filter
def query_filter(sparql_obj, fil_opts): 
    """Query the graph by given filters"""
    sparql_obj.setQuery("""
    SELECT * WHERE { 
            ?s ?p ?o .
        }
    {filter}
    """.format(filter=fil_opts))

# TODO Methode für Filter-Generierung schreiben, in die eine Liste übergeben wird 
fil_opts = "FILTER () .\nFILTER ()"
        
sparql_obj = query_all(sparql)

# Print the result
def print_res(result):
    try:
        ret = result.queryAndConvert()
        for r in ret["results"]["bindings"]:
            print(r)
    except Exception as e:
        print(e)

# Just a test term for the game search
res = search_game_name(sparql, "This Way Madness Lies")
print_res(res)