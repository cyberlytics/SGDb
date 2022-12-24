from collections import Counter
from urllib.parse import quote
from db_wrapper import query_all

"""Create multiple filter queries so it's easy to combine them."""

def convert_input(input):
    """Convert the input string(s) in the list to url encoding to make it workable for the query"""
    return [quote(i) for i in input]

def combine_Filter(filter_requests):

    """Select the filters that should be combined for the query.
    NOTE: If recommendation is used, use the objects of the game subject as the filter
    If new filters should be adapted or filters removed, pass the whole query object again to this method.
    Saves every game in the list that matches all filters.
    Matches Substrings and it is case insensitive"""
    
    game_list = []

    if "date" in filter_requests:
        if "recommendation" not in filter_requests:
            game_list = extend_list(game_list, fil_date(filter_requests["date"]))
        else: 
            pass
    if "genre" in filter_requests:
        if "recommendation" not in filter_requests:
            game_list = extend_list(game_list, fil_genre(filter_requests["genre"]))
        else: 
            game_list.append(fil_genre(filter_requests["genre"]))
    if "rating_num" in filter_requests:
        if "recommendation" not in filter_requests:
            game_list = extend_list(game_list, fil_rating(filter_requests["rating_num"]))
        else: 
            game_list.append(fil_rating(filter_requests["rating_num"]))
    if "creator" in filter_requests:
        if "recommendation" not in filter_requests:
            game_list = extend_list(game_list, fil_creator(filter_requests["creator"]))
        else: 
            game_list.append(fil_creator(filter_requests["creator"]))
    if "platform" in filter_requests:
        if "recommendation" not in filter_requests:
            game_list = extend_list(game_list, fil_platform(filter_requests["platform"]))
        else: 
            game_list.append(fil_platform(filter_requests["platform"]))
    return game_list

def extend_list(game_list, func_res, recommendation=False):
    """Only returns games that were already included in the results of other filters"""
    if(func_res):
        if len(game_list) != 0:
            # If only exact matches should be returned
            if not recommendation:
                # return only the intersections of the game_list and the results of the specific filter
                intersec = list(set(game_list).intersection(func_res))
                if intersec:
                    return intersec
                else:
                    return [None] # TODO maybe return something more meaningful
            # If recommendations should be returned
            if recommendation:
                return get_biggest_intersec(game_list)
        else:
            # if the list is empty fill it with the first results 
            return func_res 
    else:
        # If the result is None return None
        return [None]

def get_biggest_intersec(game_list):
    """Find the game which fits the other game the best"""
    return Counter(game_list).most_common()

def fil_date(year): 
    """Filter the games by the release year."""
    sparql_obj = query_all()
    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?game WHERE {{ 
        ?game schema:releaseDate ?year .
        FILTER (YEAR(?year) = {year})
        }}
        """.format(year=year))
    return extract_res(sparql_obj)
    
def fil_genre(genre): 
    """Filter the games by the given genre(s)"""
    sparql_obj = query_all()
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
    
def fil_rating(rating_num):
    sparql_obj = query_all()
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
  
def fil_creator(creator): 
    sparql_obj = query_all()
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
   

def fil_platform(platform):
    sparql_obj = query_all()
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