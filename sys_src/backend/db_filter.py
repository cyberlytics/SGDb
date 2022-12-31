from collections import Counter
from urllib.parse import quote
from SPARQLWrapper import SPARQLWrapper, JSON
import os

sparql_obj = SPARQLWrapper(os.environ.get('REPOSITORY_ADDR', "http://localhost:7200/repositories/semantic_games"))
sparql_obj.setReturnFormat(JSON)


"""Create multiple filter queries so it's easy to combine them."""

def combine_Filter(filter_requests):

    """Select the filters that should be combined for the query.
    NOTE: If recommendation is used, use the objects of the game subject as the filter
    If new filters should be adapted or filters removed, pass the whole query object again to this method.
    Saves every game in the list that matches all filters.
    Matches Substrings and it is case insensitive"""

    game_list = {}

    if "date" in filter_requests:
        if "recommendation" not in filter_requests:
            game_list = extend_list(game_list, fil_date(filter_requests["date"]))
        else: 
            pass
    if "genre" in filter_requests:
        if "recommendation" not in filter_requests:
            for element in range(len(filter_requests["genre"])):  
                game_list = extend_list(game_list, fil_genre(filter_requests["genre"][element-1]))
        else: 
            game_list.update(fil_genre(filter_requests["genre"]))
    if "rating_num" in filter_requests:
        if "recommendation" not in filter_requests:
            game_list = extend_list(game_list, fil_rating(filter_requests["rating_num"]))
        else: 
            game_list.update(fil_rating(filter_requests["rating_num"]))
    if "creator" in filter_requests:
        if "recommendation" not in filter_requests:
            for element in range(len(filter_requests["creator"])):  
                game_list = extend_list(game_list, fil_creator(filter_requests["creator"][element-1]))
        else: 
            game_list.update(fil_creator(filter_requests["creator"]))
    if "platform" in filter_requests:
        if "recommendation" not in filter_requests:
            for element in range(len(filter_requests["platform"])):  
                game_list = extend_list(game_list, fil_platform(filter_requests["platform"][element-1]))
        else: 
            game_list.update(fil_platform(filter_requests["platform"]))
    return game_list


def extend_list(game_list, func_res, recommendation=False):
    """Only returns games that were already included in the results of other filters"""
    if(func_res):
        func_res = func_res["results"]["bindings"]
        if len(game_list) != 0:
            if game_list[0] is not None:
                # If only exact matches should be returned
                if not recommendation:
                    intersec = []
                    for i in game_list:
                            for k in func_res:
                                if i["title"]["value"] == k["title"]["value"] and i not in intersec: 
                                    intersec.append(i)
                                    break
                    if intersec:
                        return intersec
                    else:
                        return [None]
            # If recommendations should be returned
            if recommendation:
                return get_biggest_intersec(game_list)

        else:
            # if the list is empty fill it with the first results 
            return func_res 
    else:
        # If the result is None return None
        return ["There is no game in the Database for the used Filter"]


def get_biggest_intersec(game_list):
    """Find the game which fits the other game the best"""
    return Counter(game_list).most_common()


def fil_date(year): 
    """Filter the games by the release year."""
    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?title ?date WHERE {{ 
        ?o schema:releaseDate ?year .
        ?o schema:title ?title .
        ?o schema:releaseDate ?date .
        FILTER (YEAR(?year) = {year})
        }}
        """.format(year=year))
    return sparql_obj.queryAndConvert()
    

def fil_genre(genre): 
    """Filter the games by the given genre(s)"""
    genre = quote(genre)
    fil_str = (f"FILTER REGEX(str(?genre), '{genre}', 'i') . ")

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?title ?date WHERE {{ 
        ?o schema:genre ?genre .
        ?o schema:title ?title .
        ?o schema:releaseDate ?date .
        {fil_str}
        }}
        """.format(fil_str=fil_str))
    return sparql_obj.queryAndConvert()
    

def fil_rating(rating_num):
    """Filter games by best score that are better than the given score number. 
    The results are descending"""

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?title ?date WHERE {{
        ?o schema:ratingValue ?rating .
        ?o schema:title ?title .
        ?o schema:releaseDate ?date .
        FILTER(?rating > "{rating_num}")
        }}
        ORDER BY DESC(?rating)
        """.format(rating_num=rating_num))
    return sparql_obj.queryAndConvert()
  

def fil_creator(creator): 
    """Filter the games by the producer"""
    creator = quote(creator)
    fil_str = (f"FILTER REGEX(str(?creator), '{creator}', 'i') . ")

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?title ?date WHERE {{
        ?o schema:creator ?creator .
        ?o schema:title ?title .
        ?o schema:releaseDate ?date .
        {fil_str}
        }}
        """.format(fil_str=fil_str))
    return sparql_obj.queryAndConvert()
   

def fil_platform(platform):
    """Filter the games by their platform(s). Like ['Nintendo', 'Sony']."""
    platform = quote(platform)
    fil_str = (f"FILTER REGEX(str(?platform), '{platform}', 'i') . ")

    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?title ?date WHERE {{
        ?o schema:gamePlatform ?platform .
        ?o schema:title ?title .
        ?o schema:releaseDate ?date .
        {fil_str}
        }}
        """.format(fil_str=fil_str))
    return sparql_obj.queryAndConvert()