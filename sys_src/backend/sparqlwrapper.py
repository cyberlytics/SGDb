from SPARQLWrapper import SPARQLWrapper, JSON

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

# todo: query for filter-options; load new graph with filter(s) activated
    # param1: sparql object, which is generated in this file
    # param2: filter-options from main.py
    # return json with new graph