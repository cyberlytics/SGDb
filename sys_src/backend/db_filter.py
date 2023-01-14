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

    if "date" in filter_requests and filter_requests["date"] != "":
        game_list = extend_list(game_list, fil_date(filter_requests["date"]))

    if "rating_num" in filter_requests and filter_requests["rating_num"] != "":
        game_list = extend_list(game_list, fil_rating(filter_requests["rating_num"]))

    if "genre" in filter_requests:
        for element in filter_requests["genre"]:  
                game_list = extend_list(game_list, fil_genre(element))

    if "creator" in filter_requests:
        for element in filter_requests["creator"]:  
                game_list = extend_list(game_list, fil_creator(element))

    if "platform" in filter_requests:
        for element in filter_requests["platform"]:  
                game_list = extend_list(game_list, fil_platform(element))

    return game_list


def recommendations(content_detailpage):
    games = []
    if "genreNames" in content_detailpage: 
        for element in content_detailpage["genreNames"]["value"].split(","):
            res = fil_genre(element)
            games.extend(get_titles(res))
    if "creatorNames" in content_detailpage: 
        for element in content_detailpage["creatorNames"]["value"].split(","):
            res = fil_creator(element)
            games.extend(get_titles(res))
    if "gamePlatformNames" in content_detailpage: 
        for element in content_detailpage["gamePlatformNames"]["value"].split(","):
            res = fil_genre(element)
            games.extend(get_titles(res))

    recomms =  get_biggest_intersec(games, content_detailpage["title"]["value"])
    if recomms is None:
        return None
    else:
        return get_imgs(recomms)


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
        mc_games = Counter(results).most_common(5)
        return [game[0] for game in mc_games]
    else:
        return None

def get_imgs(mc_games):
    """Get the images and titles of the n recommended games"""
    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?title ?image WHERE {{ 
            VALUES ?title {{
            "{mc_games[0]}"
            "{mc_games[1]}"
            "{mc_games[2]}"
            "{mc_games[3]}"
            "{mc_games[4]}"
            }}
            ?s schema:title ?title .
            ?s schema:image ?image .
        }}
        """.format(mc_games=mc_games))
    conv_obj = sparql_obj.queryAndConvert()
    return conv_obj["results"]["bindings"]

def extend_list(game_list, func_res):
    """Only returns games that were already included in the results of other filters"""
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
            return [None]
    else:
        # if the list is empty fill it with the first results 
        return func_res 


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