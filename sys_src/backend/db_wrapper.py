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


# query for search; search after game-name
    # param1: sparql object, which is generated in this file
    # param2: game-name from main.py
    # return json with possible games

def search_subject_to_query(sparql_obj, game_name):
    # Search the subject to the game name, case-insensitive
    # if there are more than one game, return all subjects
    sparql_obj.setQuery("""
        PREFIX schema: <http://schema.org/>
        SELECT ?s ?p ?o WHERE {{ 
        ?o schema:title ?title .
        FILTER REGEX(?title, "{game_name}", "i")
        }}
        """.format(game_name=game_name))
    subject = sparql_obj.query().convert()
    subject_list = []
    # save all possible subjects in a list
    for i in range(len(subject["results"]["bindings"])):
        subject_list.append(subject["results"]["bindings"][i]["o"]["value"])
    return subject_list

# method for searching games
def search_query(sparql_obj, game_name):
    subject_iris = search_subject_to_query(sparql_obj, game_name)
    if len(subject_iris) != 1:
        result = []
        # if there are more than one search result, append them to a list and return the list
        for i in range(len(subject_iris)):
            result.append(query_the_subject(sparql_obj, subject_iris[i]))
            result[i] = result[i]["results"]["bindings"]
        return result
    # if there is only one search result, give only that one back
    # return empty list if there is no game found
    else:
        result = query_the_subject(sparql_obj, subject_iris[0])
        result = result["results"]["bindings"]
        return result
    

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