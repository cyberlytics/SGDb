from SPARQLWrapper import SPARQLWrapper, JSON
from db_filter import fil_date
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
        PREFIX schema: <https://schema.org/>
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
        PREFIX schema: <https://schema.org/>
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
    # in the result list all posible findings will be saved and returned
    result = []
    for i in range(len(subject_iris)):
        result.append(query_the_subject(sparql_obj, subject_iris[i]))
        result[i] = result[i]["results"]["bindings"]
    return result


# method to get root-graph dependent on the release date of a game
def get_root_graph(sparql_obj):
    root_graph = {}
    # get all games from 1950 to 2022
    for year in range(1950, 2022):
        # save the iri of the games in the specific year of the for loop
        games_in_year = fil_date(sparql_obj, year)
        # if there is no game in the year it should skip the year
        if len(games_in_year) == 0: continue
        # if there are more games in a particular year it should save all in a list well formated
        for game in range(len(games_in_year)):
            games_in_year[game] = query_the_subject(sparql_obj, games_in_year[game])
            games_in_year[game] = games_in_year[game]["results"]["bindings"]
        # add to a dictonary the years as key and the games of that particular year as value
        root_graph[year]=games_in_year
    return root_graph


# todo: query for filter-options; load new graph with filter(s) activated
    # param1: sparql object, which is generated in this file
    # param2: filter-options from main.py
    # return json with new graph