from SPARQLWrapper import SPARQLWrapper, JSON
from collections import Counter
import json

graphdb_url = "http://localhost:7200/repositories/semantic_games"
sparql_obj = SPARQLWrapper(graphdb_url)
sparql_obj.setReturnFormat(JSON)

"""This methods help to get a list for the filters in the frontend
with all or the most frequent values from the database by a given schema type"""

def get_filter_vals(sparql_obj, schema_type, top_n=True):
    """Use the filter_schema method and put them into extract_obj 
    to get a list of the preferenced values"""
    res = filter_schema(sparql_obj, schema_type)
    res_list = extract_obj(res)
    if top_n:
        return get_most_frequents(res_list, 15)
    else:
        return res_list

def filter_schema(sparql_obj, schema_type):
    """get the objects which fit the choosen schema type"""
    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?object WHERE {{ 
        ?game schema:{schema_type} ?object.
        }}                  
        """.format(schema_type=schema_type))
    return extract_obj(sparql_obj)

def extract_obj(result):
    """get the objects inside a list"""
    try:
        ret = result.queryAndConvert()
        objs = ret["results"]["bindings"]
        return [obj["object"]["value"] for obj in objs]
    except Exception as e:
        print(e)

def get_most_frequents(type_list, n):
    """return the n most common values in a list"""
    return [val for val, count in Counter(type_list).most_common(n)]

def save_as_json(*val_lists):
    """Save the lists as JSON data"""
    with open("filter_values.json", "w") as f:
        for data in val_lists:
            json.dump(data, f, indent=4)

# Generate lists for the given filters 
genre_list = {"genre" : get_filter_vals(sparql_obj, "genre")}
# date_list = {"releaseDate" : get_filter_vals(sparql_obj, "releaseDate", False)} # is it even necessary??
# rating_list = {"ratingValues" : get_filter_vals(sparql_obj, "ratingValues")} # not necessary 'cause they are always from 1 to 100
creator_list = {"creator" : get_filter_vals(sparql_obj, "creator")}
platform_list = {"platform" : get_filter_vals(sparql_obj, "platform")}

# Save all lists in a json file
save_as_json(genre_list, creator_list, platform_list)