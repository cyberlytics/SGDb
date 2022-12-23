from SPARQLWrapper import SPARQLWrapper, JSON
import os

# Get the url to the graphdb repository
graphdb_url = 'http://' + os.environ.get('DB_ADDR') + '/repositories/semantic_games'
# keep the next line for easy debug purpose
#graphdb_url = "http://localhost:7200/repositories/semantic_games"

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

# get root graph with title and releaseDate
def get_root_graph():
    sparql_obj = query_all()
    sparql_obj.setQuery("""
    PREFIX schema: <https://schema.org/>
    SELECT ?year ?title WHERE {{ 
    ?o schema:releaseDate ?year .
    ?o schema:title ?title .
    }}""")
    return(sparql_obj.query().convert())

# query for detailpage; content for detail page
    # param1: sparql object, which is generated in the main.py file
    # param2: game-name from main.py
    # return json with content of detail page to particular game

def subject_to_query(game_name):
    sparql_obj = query_all()
    # Search the subject to the game name
    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?s ?p ?o WHERE {{ 
        ?o schema:title "{game_name}" .
        }}
        """.format(game_name=game_name))
    subject = sparql_obj.query().convert()
    if not subject["results"]["bindings"]:
        return None
    return subject["results"]["bindings"][0]["o"]["value"]
    
def query_the_subject(subject):
    # Search the Query by the given subject
    sparql_obj = query_all()
    sparql_obj.setQuery("""
        SELECT ?subject ?predicate ?object
        WHERE {{
            <{subject}> ?predicate ?object .
        }} LIMIT 100
        """.format(subject=subject))
    return sparql_obj.query().convert()

# method for searching games with their title
def detailpage_content(game_name):
    subject_iri = subject_to_query(game_name)
    if subject_iri is None:
        return {"error": "No game found"}
    result = query_the_subject(subject_iri)
    bindings = result['results']['bindings']
    res = {b['predicate']['value'].split('/')[-1]: b['object']['value'] for b in bindings}
    return res


# query for search; search after game-name
    # param1: sparql object, which is generated in this file
    # param2: game-name from main.py
    # return json with possible games

def search_subject_to_query(game_name):
    sparql_obj = query_all()
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
def search_query(game_name):
    subject_iris = search_subject_to_query(game_name)
    # in the result list all posible findings will be saved and returned
    result = []
    for i in range(len(subject_iris)):
        result.append(query_the_subject(subject_iris[i]))
        result[i] = result[i]["results"]["bindings"]
    return result

