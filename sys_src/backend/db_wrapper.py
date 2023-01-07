from SPARQLWrapper import SPARQLWrapper, JSON
import os

# db object initialize
graphdb = SPARQLWrapper(os.environ.get('REPOSITORY_ADDR', "http://localhost:7200/repositories/semantic_games"))
graphdb.setReturnFormat(JSON)


# get root graph with title and releaseDate
def get_root_graph():
    graphdb.setQuery("""
    PREFIX schema: <https://schema.org/>
    SELECT ?year ?title WHERE {{ 
    ?o schema:releaseDate ?year .
    ?o schema:title ?title .
    }}""")
    return graphdb.query().convert()

def query_game_details(title: str):
    """Query game details by title"""

    graphdb.setQuery("""
        PREFIX schema: <https://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT *
        WHERE {{
        ?game rdf:type schema:VideoGame .
        ?game schema:title ?title .
        ?game schema:releaseDate ?releaseDate .
        ?game schema:image ?image .
        ?game schema:ratingValue ?ratingValue .
        ?game schema:description ?description .
        ?game schema:creator ?creator .
        ?creator schema:name ?creatorName .
        ?game schema:gamePlatform ?gamePlatform .
        ?gamePlatform schema:name ?gamePlatformName .
        ?game schema:genre ?genre .
        ?genre schema:name ?genreName .
        FILTER REGEX(?title, "{game_name}", "i")
        }}
        """.format(game_name=title))
    return graphdb.query().convert()


def detailpage_content(game_name: str):
    result = query_game_details(game_name)
    if len(result["results"]["bindings"]) == 0:
        return None
    bindings = result['results']['bindings'][0]
    return bindings

# method for searching games
def search_query(game_name):
    graphdb.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?title WHERE {{ 
        ?o schema:title ?title .
        FILTER REGEX(?title, "{game_name}", "i")
        }}
        """.format(game_name=game_name))
    searched_games = graphdb.query().convert()
    return searched_games