from filter_lists import get_filter_vals, extract_obj, get_most_frequents

def test_get_filter_vals():
    # Call the `get_filter_vals` function with a sample input
    data = get_filter_vals("genre", top_n=True)

    # Check that the output is a list of dictionaries
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

    # Check that the list contains dictionaries with a single key-value pair
    assert all(len(item) == 1 for item in data)

def test_get_filter_vals_with_false_top_n():
    # Call the `get_filter_vals` function with a sample input
    data = get_filter_vals("genre", top_n=False)

    # Check that the output is a list of strings
    assert isinstance(data, list)
    assert all(isinstance(item, str) for item in data)

    # Check that the list has over 1000 entries.
    # because there are 500 games, every game should have atleast 2 genres
    assert len(data) > 1000

def test_extract_obj():
    # Create a sample input
    result = {
        "results": {
            "bindings": [
                {"object": {"value": "http://example.com/base/Shooter"}},
                {"object": {"value": "http://example.com/base/Indie"}},
            ]
        }
    }

    # Call the `extract_obj` function with the sample input
    data = extract_obj(result)

    # Check that the output is a list of strings
    assert isinstance(data, list)
    assert all(isinstance(item, str) for item in data)

    # Check that the list contains the expected values
    assert data == ["http://example.com/base/Shooter", "http://example.com/base/Indie"]

# test if the result ist wrong formated
def test_extract_obj_exception():
    result = ""
    assert extract_obj(result) == None


def test_get_most_frequents():
    # Create a sample input
    type_list = ["indie", "shooter", "indie"]

    # Call the `get_most_frequents` function with the sample input
    data = get_most_frequents(type_list, n=None)

    # Check that the output is a list of dictionaries
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)

    # Check that the list contains dictionaries with a single key-value pair
    assert all(len(item) == 1 for item in data)

    # Check that the dictionaries contain the expected keys and values
    assert data == [{"indie": 2}, {"shooter": 1}]