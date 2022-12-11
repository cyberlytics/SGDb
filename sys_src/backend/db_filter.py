from urllib.parse import quote
from db_wrapper import query_the_subject


# from SPARQLWrapper import SPARQLWrapper, JSON

# graphdb_url = "http://localhost:7200/repositories/semantic_games"
# sparql_obj = SPARQLWrapper(graphdb_url)
# sparql_obj.setReturnFormat(JSON)


## Create multiple filter queries so it's easy to combine them ###
# There should be always send a copy to the query so the original sparql obj is fastly available

def convert_input(input):
    """Convert the input string(s) in the list to url encoding to make it workable for the query"""
    return [quote(i) for i in input]

def combine_Filter(
    sparql_obj, 
    date=None, 
    genre = None,
    rating_num=None, 
    creator=None, 
    platform=None):

    """Select the filters that should be combined for the query.
    If new filters should be adapted or filters removed, pass the whole query object again to this method.
    Saves every game in the list that matches all filters.
    Matches Substrings and it is case insensitive"""

    game_list = []

    if date:
        game_list = extend_list(game_list, fil_date(sparql_obj, date))
    if genre:
        game_list = extend_list(game_list, fil_genre(sparql_obj, genre))
    if rating_num:
        game_list = extend_list(game_list, fil_rating(sparql_obj, rating_num))
    if creator:
        game_list = extend_list(game_list, fil_creator(sparql_obj, creator))
    if platform:
        game_list = extend_list(game_list, fil_platform(sparql_obj, platform))
    return game_list

def extend_list(game_list, func_res):
    """Only returns games that were already included in the results of other filters"""
    if(func_res):
        if len(game_list) != 0:
            # return only the intersections of the game_list and the results of the specific filter
            intersec = list(set(game_list).intersection(func_res))
            if intersec:
                return intersec
            else:
                return [None] # TODO maybe return something more meaningful
        else:
            # if the list is empty fill it with the first results 
            return func_res 
    else:
        # If the result is None return None
        return [None]

def fil_date(sparql_obj, year): 
    """Filter the games by the release year."""

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?game WHERE {{ 
        ?game schema:releaseDate ?year .
        FILTER (YEAR(?year) = {year})
        }}
        """.format(year=year))
    return extract_res(sparql_obj)
    
def fil_genre(sparql_obj, genre): 
    """Filter the games by the given genre(s)"""
    genre = convert_input(genre)
    fil_str = create_filter("?genre", genre)

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?game WHERE {{ 
        ?game schema:genre ?genre .
        {fil_str}
        }}
        """.format(fil_str=fil_str))
    return extract_res(sparql_obj)
    
def fil_rating(sparql_obj, rating_num):
    """Filter games by best score that are better than the given score number. 
    The results are descending"""

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?game WHERE {{
        ?game schema:ratingValue ?rating .
        FILTER(?rating > "{rating_num}")
        }}
        ORDER BY DESC(?rating)
        """.format(rating_num=rating_num))
    return extract_res(sparql_obj)
  
def fil_creator(sparql_obj, creator): 
    """Filter the games by the producer"""
    creator = convert_input(creator)
    fil_str = create_filter("?creator", creator)

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?game WHERE {{
        ?game schema:creator ?creator .
        {fil_str}
        }}
        """.format(fil_str=fil_str))
    # FILTER (lcase(str(?o)) = "red")
    return extract_res(sparql_obj)
   

def fil_platform(sparql_obj, platform):
    """Filter the games by their platform(s). Like ['Nintendo', 'Sony']."""
    platform = convert_input(platform)
    fil_str = create_filter("?platform", platform)

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?game WHERE {{
        ?game schema:gamePlatform ?platform .
        {fil_str}
        }}
        """.format(fil_str=fil_str))
    return extract_res(sparql_obj)

def create_filter(type, arg_list):
    """Create a Query string for a name search filter method by n given arguments
    and returns a n long Filter as a string"""
    fil_str= ""
    for arg in arg_list:
        fil_str += (f"FILTER REGEX(str({type}), '{arg}', 'i') . ")
    return fil_str

def extract_res(result):
    """get the games themself as subjects inside a list"""
    try:
        ret = result.queryAndConvert()
        games = ret["results"]["bindings"]
        return [game["game"]["value"] for game in games]
    except Exception as e:
        print(e)

# # Test it with arguments
# res = combine_Filter(
#     sparql_obj, 
#     date=None,
#     genre=["Adventure", "rpg"],
#     rating_num=90, 
#     creator=["nintendo"], 
#     platform=None
#     )

# # Give all subs into query and return the subs, preds and obs
# if res[0]:
#     for r in res:
#         print(query_the_subject(sparql_obj, r))
# else:
#     print("No results found")