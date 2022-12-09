### Create multiple filter queries so it's easy to combine them by their query ###
# TODO Problem: Wenn Filter rückgängig gemacht, vorherigen zustand wieder herstellen. 
# TODO Es sollte im Backend immer eine graphen copy an den filter gesendet werden

def select_Filter(sparql, date=False, genre=False, score=False, producer=False, platform=False):

    # TODO Bezug in einzelnen Filtern immer nur das Spiel als Ausgabe und Gesamtausgabe dieser Methode dann alle zugehörigen Entitäten zum Spiel?
    # TODO Param-Übergabe wie range, genre etc.
    """Select the filters that should be combined for the query
    If new filters should be adapted or filters removed, pass the whole query object again to this method"""
    if date:
        sparql = fil_date(sparql)
    if genre:
        sparql = fil_genre(sparql)
    if score:
        sparql = fil_score(sparql)
    if producer:
        sparql = fil_producer(sparql)
    if platform:
        sparql = fil_platform(sparql)
    return convert_res(sparql)

def fil_date(sparql, date, range=False, newer=True):
    """Filter the games by the release year. Filter for matches by an exact year or a range like older or newer released than {year}."""
    sparql.setQuery("""
        PREFIX schema: <http://schema.org/>
        SELECT ?s ?p ?o WHERE {{ 
        ?o schema:release_day "{game_name}" .
        }}
        """.format(date=date))
    return sparql

def fil_genre(sparql, genre): # ATM only one genre to filter
    """Filter the games by the given genre"""
    return sparql

def fil_score(sparql): # TODO Im frontend queryergebnisse einfach umdrehen, falls nach schlechtesten gesucht werden soll. erspart aufwand
    """Filter games by best scores. The results are descending"""
    return sparql

# TODO Sinnvoll eine get methode zu implementieren, die dem frontend alle genres übergibt?
def fil_producer(sparql): 
    """Filter the games by the producer"""
    # FILTER (lcase(str(?o)) = "red")
    return sparql

def fil_platform(sparql, platform): # TODO Sinnvoll eine get methode zu implementieren, die dem frontend alle plattformen übergibt?
    # TODO man könnte auch die most frequent nehmen
    """Filter the games by their platform. Like 'Nintendo' or 'Sony'."""
    return sparql

def convert_res(result):
    """Converts the sparqle object to usable JSON format for frontend"""
    try:
        ret = result.queryAndConvert()
        return [r for r in ret["results"]["bindings"]]  
    except Exception as e:
        print(e)