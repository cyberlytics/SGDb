from db_filter import recommendations, get_titles

# test the return value, if there is no valid detailpage is returned
def test_recommendations_no_data():
    content_detailpage = {
    "title": {
        "value": "test_val"
    }
}
    assert recommendations(content_detailpage) == None

# test if the response type is correct
# test if all values are returned
# test if the duplicated values are returned only once
def test_get_titles():
    para = {"results": {"bindings": [{"title": {"value": "test_game_1"}}, {"title": {"value": "test_game_1"}}, {"title": {"value": "test_game_2"}}]}}
    result = get_titles(para)
    expected_titles = ["test_game_1", "test_game_2"]
    assert result == expected_titles
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)

