from collections import Counter
from urllib.parse import quote
from SPARQLWrapper import SPARQLWrapper, JSON
from db_wrapper import detailpage_content
import os

sparql_obj = SPARQLWrapper(os.environ.get('REPOSITORY_ADDR', "http://localhost:7200/repositories/semantic_games"))
sparql_obj.setReturnFormat(JSON)


"""Create multiple filter queries so it's easy to combine them."""

def combine_Filter(filter_requests, recommendation=False):

    """Select the filters that should be combined for the query.
    NOTE: If recommendation is used, use the objects of the game subject as the filter
    If new filters should be adapted or filters removed, pass the whole query object again to this method.
    Saves every game in the list that matches all filters.
    Matches Substrings and it is case insensitive"""

    game_list = {}
    games = []
    
    if "date" in filter_requests and filter_requests["date"] != "":
        if recommendation is False:
            game_list = extend_list(game_list, fil_date(filter_requests["date"]))

    if "rating_num" in filter_requests and filter_requests["rating_num"] != "":
        if recommendation is False:
            game_list = extend_list(game_list, fil_rating(filter_requests["rating_num"]))

    if "genre" in filter_requests:
        if recommendation is False:
            for element in filter_requests["genre"]:  
                game_list = extend_list(game_list, fil_genre(element))
        elif "genreName" in filter_requests: 
            for element in filter_requests["genreName"]["value"].split(","):
                res = fil_genre(element)
                games.extend(get_titles(res))

    if "creator" in filter_requests:
        if recommendation is False:
            for element in filter_requests["creator"]:  
                game_list = extend_list(game_list, fil_creator(element))
        elif "creatorName" in filter_requests: 
            for element in filter_requests["creatorName"]["value"].split(","):
                res = fil_creator(element)
                games.extend(get_titles(res))

    if "platform" in filter_requests:
        if recommendation is False:
            for element in filter_requests["platform"]:  
                game_list = extend_list(game_list, fil_platform(element))
        elif "gamePlatformName" in filter_requests: 
            for element in filter_requests["gamePlatformName"]["value"].split(","):
                res = fil_genre(element)
                games.extend(get_titles(res))

    if recommendation is False:
        return game_list
    else: 
        return get_biggest_intersec(games, filter_requests["title"]["value"])
        

def get_titles(result):
    """Extract the Titles of a game dictionary"""
    games = [] 
    result = result["results"]["bindings"]
    for game in result:
        if game["title"]["value"] not in games:
            games.append(game["title"]["value"])
    return games


def get_biggest_intersec(results, title):
    """Find the game which fits the given game the best by counting similiar attributes 
    and return the game with the most similiar attributes"""
    if results != []:
        # remove all titles of the list which matches the title of the given game
        results = [game for game in results if game != title]
        # Search for the most common game name
        mc_games = Counter(results).most_common(1)
        return mc_games[0][0]
    else:
        return None


def extend_list(game_list, func_res):
    """Only returns games that were already included in the results of other filters"""
    if(func_res):
        func_res = func_res["results"]["bindings"]
        if len(game_list) != 0:
            if game_list[0] is not None:
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
        else:
            # if the list is empty fill it with the first results 
            return func_res 
    else:
        # If the result is None return None
        return ["There is no game in the Database for the used Filter"]


def fil_date(year): 
    """Filter the games by the release year"""
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