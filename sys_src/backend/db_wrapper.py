from SPARQLWrapper import SPARQLWrapper, JSON
from typing import Optional

# for debugging purpose
import uvicorn

# Get the url to the graphdb repository
graphdb_url = "http://localhost:7200/repositories/semantic_games"

# Query for whole Graph
def query_all():
    # db object initialize
    sparql = SPARQLWrapper(graphdb_url)
    sparql.setReturnFormat(JSON)

    """Queries the whole graph and returns it"""
    sparql.setQuery("""
        SELECT * WHERE { 
            ?s ?p ?o .
        }
    """)
    return sparql


# query for detailpage; content for detail page
    # param1: sparql object, which is generated in the main.py file
    # param2: game-name from main.py
    # return json with content of detail page to particular game
# Case-sensitve atm, should be changed to case-insensitive

def subject_to_query(sparql_obj, game_name):
    # Search the subject to the game name
    sparql_obj.setQuery("""
        PREFIX schema: <http://schema.org/>
        SELECT ?s ?p ?o WHERE {{ 
        ?o schema:title "{game_name}" .
        }}
        """.format(game_name=game_name))
    subject = sparql_obj.query().convert()
    return subject["results"]["bindings"][0]["o"]["value"]
    
def query_the_subject(sparql_obj, subject):
    # Search the Query by the given subject
    sparql_obj.setQuery("""
        SELECT ?subject ?predicate ?object
        WHERE {{
            <{subject}> ?predicate ?object .
        }} LIMIT 100
        """.format(subject=subject))
    return sparql_obj.query().convert()

# Print the result
def print_result(result):
    try:
        for r in result["results"]["bindings"]:
            print(r)
    except Exception as e:
        print(e)

# method for searching games with their title
def detailpage_content(sparql_obj, game_name):
    subject_iri = subject_to_query(sparql_obj, game_name)
    result = query_the_subject(sparql_obj, subject_iri)
    return result


#############################################################
# still under construction under this section
#############################################################
# query for search; search after game-name
    # param1: sparql object, which is generated in this file
    # param2: game-name from main.py
    # return json with possible games
# Case-sensitve atm, should be changed to case-insensitive
# should be working like igdb search
'''
def search_game_name(sparql_obj, game_name):
    # Search the Query for the subject by the given game name
    sparql_obj.setQuery("""
        PREFIX schema: <http://schema.org/>
        SELECT ?s ?p ?o WHERE {{ 
        ?o schema:title "{game_name}" .
        }}
        """.format(game_name=game_name))
    subject = sparql_obj.query().convert()
    subject_name = subject["results"]["bindings"][0]["o"]["value"]
    sparql_obj.setQuery("""
        SELECT ?subject ?predicate ?object
        WHERE {
            <{subject_name}> ?predicate ?object .
        }
    """)
    result_to_formated = sparql_obj.query().convert()
    result = {}
    for r in result_to_formated["results"]["bindings"]:
        result.update(r)
    return result
'''
'''
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
'''
    

# todo: query for filter-options; load new graph with filter(s) activated
    # param1: sparql object, which is generated in this file
    # param2: filter-options from main.py
    # return json with new graph
    
'''
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
'''