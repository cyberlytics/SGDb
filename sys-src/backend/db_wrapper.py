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

# Query for Detailpage, return only one entry. The cells with different results will be grouped.
def query_game_details(title: str):
    graphdb.setQuery("""
        PREFIX schema: <https://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?game ?title (GROUP_CONCAT(DISTINCT ?releaseDate; separator = ", ") as ?releaseDate) (GROUP_CONCAT(DISTINCT ?image; separator = ", ") as ?image) 
        (GROUP_CONCAT(DISTINCT ?ratingValue; separator = ", ") as ?ratingValue) (GROUP_CONCAT(DISTINCT ?description; separator = ", ") as ?description)
        (GROUP_CONCAT(DISTINCT ?creatorName; separator = ", ") as ?creatorNames) (GROUP_CONCAT(DISTINCT ?gamePlatformName; separator = ", ") as ?gamePlatformNames)
        (GROUP_CONCAT(DISTINCT ?genreName; separator = ", ") as ?genreNames)
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
        GROUP BY ?game ?title
        """.format(game_name=title))
    return graphdb.query().convert()


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