from fastapi.testclient import TestClient
from db_wrapper import query_game_details
from filter_lists import get_data
from db_filter import recommendations
from main import app

client = TestClient(app)

#############################
# tests for GET startpage
#############################
# test if the startpage return structure is correct
def test_startpage_structure():
    response = client.get('/')
    assert isinstance(response.json(), dict)
    assert 'data' in response.json()
    assert 'filters' in response.json()
    assert response.status_code == 200

# test if the returned filter count is correct
def test_startpage_num_filters():
    response = client.get('/')
    assert len(response.json()['filters']) == len(get_data())

# test if all filters are in the startpage response
def test_startpage_return_filters():
    response = client.get('/')
    assert "genre" in response.json()['filters']
    assert "creator" in response.json()['filters']
    assert "platform" in response.json()['filters']

# test if there is a node in the the graph
def test_startpage_title_for_year():
    response = client.get('/')
    assert len(response.json()["data"]) == 38
    assert response.json()["data"]["1989"] == ["Denaris"]

#############################
# tests for POST startpage
#############################
# Test that the startpage endpoint returns the expected output
def test_post_startpage():
    response = client.post("/", json={"date": 2013, "genre": "shooter", "platform": "Playstation 3", "rating_num": 50})
    assert response.status_code == 200
    assert "The Last of Us" in response.json()["data"]["2013"]

# test if only the date filter is used
def test_post_only_date():
    response = client.post("/", json={"date": 1994})
    assert response.status_code == 200
    assert "Super Metroid" in response.json()["data"]["1994"]

# test if only the creator filter is used
def test_post_only_creator():
    response = client.post("/", json={"creator": "Nintendo"})
    assert response.status_code == 200
    assert "Punch-Out!!" in response.json()["data"]["1983"]

# Test that the startpage endpoint returns the expected output
def test_post_no_matching_game():
    response = client.post("/", json={"date": 2013, "genre": "shooter", "platform": "Playstation 3", "rating_num": 93})
    assert response.status_code == 404
    assert response.json() == {"message": "no matching game with the used filter"}

# Test that the startpage endpoint returns the expected output
def test_post_startpage_years():
    response = client.post("/", json={"date": [2010, 2020]})
    assert response.status_code == 404
    assert response.json() == {"message": "invalid date input, only int allowed"}

# Test that the startpage endpoint returns the expected output
def test_post_startpage_ratingnum():
    response = client.post("/", json={"rating_num": [50, 95]})
    assert response.status_code == 404
    assert response.json() == {"message": "invalid rating_num input, only int allowed"}

# Test that the startpage endpoint returns the expected output
def test_post_startpage_no_matching_game():
    response = client.post("/", json={"date": 1950, "genre": ["puzzle", "simulator", "adventure", "shooter"]})
    assert response.status_code == 404
    assert response.json() == {"message": "no matching game with the used filter"}

#############################
# tests for search
#############################
# test if a search request with multiple games are correct
def test_search():
    response = client.get('/search/eve')
    assert response.status_code == 200
    eve_in_search = False
    for match in response.json()["matches"]:
        if str(match).find("eve") != -1:
            eve_in_search = True
    assert eve_in_search == True
    
# test if it's only a single game with the searched name
def test_search_single():
    response = client.get('/search/Evergate')
    assert response.status_code == 200
    assert response.json()["matches"][0] == "Evergate"
    assert len(response.json()["matches"]) == 1

# a warining appears. but it has to be "\\\(" escaped, because the db need two "\\" for the escaping
def test_search_escaping():
    response = client.get('/search/chrono_trigger_(2008)')
    assert response.status_code == 200
    assert response.json()["matches"][0] == "Chrono Trigger (2008)"

# test if search find no matching game
def test_search_no_match():
    response = client.get('/search/xxxxxxx')
    assert response.status_code == 404
    assert response.json() == {"message": "searched game not found"}

# test if search results are in the un/filtered graph
def test_search_in_graph():
    response = client.get('/')
    response = client.get('/search/ku')
    assert response.status_code == 200
    assert "Sengoku Rance" in response.json()["match_in_graph"]
    assert "Carol Vorderman's Sudoku" in response.json()["match_in_graph"]
    assert len(response.json()["match_in_graph"]) == 2

# test if one search result is in the graph and one result out of the graph
def test_search_out_graph():
    response = client.post("/", json={"genre": "puzzle"})
    response = client.get('/search/ku')
    assert response.status_code == 200
    assert response.json()["match_in_graph"][0] == "Carol Vorderman's Sudoku"
    assert response.json()["match_out_graph"][0] == "Sengoku Rance"
    assert len(response.json()["match_in_graph"]) == 1
    assert len(response.json()["match_out_graph"]) == 1

# test if there is no title for search
def test_search_with_no_content():
    response = client.get('/search/')
    assert response.status_code == 200
    assert response.json() == {"message": "please enter a title for search"}

#############################
# tests for detailpage
#############################
# test if a detailpage is shown and recommendations are added
def test_detailpage():
    response = client.get('/detail/Evergate')
    assert response.status_code == 200
    response_detailpage = {key: value for key, value in response.json().items() if key != "recommends"}
    detailpage = query_game_details("Evergate")
    detailpage = detailpage['results']['bindings'][0]
    recommends = recommendations(detailpage)

    assert detailpage == response_detailpage
    assert recommends == response.json()["recommends"]

# test if a title is used for the detailpage, that doesn´t exist
def test_detailpage_no_input():
    response = client.get('/detail/xxxxxxx')
    assert response.status_code == 404
    assert response.json() == {"message": "no game for detailpage found"}