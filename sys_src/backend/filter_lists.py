from collections import Counter
from urllib.parse import unquote
import json
from db_wrapper import query_all

"""This methods help to get a list for the filters in the frontend
with all or the most frequent values from the database by a given schema type"""


def get_filter_vals(schema_type, top_n=True):
    """Use the filter_schema method and put them into extract_obj to get
    a list of the preferenced values. Use regex to get only the value without the URL syntax"""
    res = filter_schema(schema_type)
    res_list = extract_obj(res)
    reg_list = use_regex(res_list)
    if top_n:
        return get_most_frequents(reg_list, 15)
    else:
        return reg_list


def filter_schema(schema_type):
    """get the objects which fit the choosen schema type"""
    sparql_obj = query_all()
    sparql_obj.setQuery("""
        PREFIX schema: <https://schema.org/>
        SELECT ?object WHERE {{ 
        ?game schema:{schema_type} ?object.
        }}                  
        """.format(schema_type=schema_type))
    return sparql_obj


def extract_obj(result):
    """get the objects inside a list"""
    try:
        ret = result.queryAndConvert()
        objs = ret["results"]["bindings"]
        return [obj["object"]["value"] for obj in objs]
    except Exception as e:
        print(e)


def use_regex(result):
    """Get only the name instead of the whole IRI"""
    # Extract only the last element of the URL
    # remove unnecessary chars from url syntax
    clean_l = []
    for e in result:
        e = e.split("/")[-1]  # [^\/]+$ works as well
        e = unquote(e)
        clean_l.append(e)
    return clean_l


def get_most_frequents(type_list, n):
    """return the n most common values in a list"""
    return [{val: count} for val, count in Counter(type_list).most_common(n)]


def save_as_json(*val_lists):
    """Save the lists as JSON data"""
    with open("./frontend/src/lib/stores/filter_values.json", "w") as f:
        for data in val_lists:
            json.dump(data, f, indent=4)


def get_data():
    # Generate lists for the given filters 
    genre_list = {"genre": get_filter_vals("genre")}
    # date_list = {"releaseDate" : get_filter_vals(sparql_obj, "releaseDate", False)} # is it even necessary??
    # rating_list = {"ratingValues" : get_filter_vals(sparql_obj, "ratingValues")} # not necessary 'cause they are always from 1 to 100
    creator_list = {"creator": get_filter_vals("creator")}
    platform_list = {"platform": get_filter_vals("gamePlatform")}
    return [genre_list, creator_list, platform_list]

# Save all lists in a json file
# save_as_json(genre_list, creator_list, platform_list)
