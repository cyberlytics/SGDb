from fastapi.testclient import TestClient
from db_wrapper import detailpage_content
from filter_lists import get_data
from main import app

client = TestClient(app)

def test_startpage_structure():
    response = client.get('/')
    assert isinstance(response.json(), dict)
    assert 'data' in response.json()
    assert 'filters' in response.json()
    assert response.status_code == 200

def test_startpage_num_filters():
    response = client.get('/')
    assert len(response.json()['filters']) == len(get_data())

def test_startpage_title_for_year():
    response = client.get('/')
    assert len(response.json()["data"]) == 38
    assert response.json()["data"]["1989"] == ["Denaris"]
    
def test_post_startpage():
    # Test that the startpage endpoint returns the expected output
    response = client.post("/", json={"date": "2013", "genre": "shooter", "gamePlatform": "Playstation 3"})
    assert response.status_code == 200
    assert "The Last of Us" in response.json()["data"]["2013"]

# test if a search request with multiple games are correct
def test_search():
    response = client.get('/search/eve')
    assert response.status_code == 200
    assert any(str(match).find("eve") != -1 for match in response.json()["matches"])
    
# test if it's only a single game with the searched name
def test_search_single():
    response = client.get('/search/Evergate')
    assert response.status_code == 200
    assert response.json()["matches"][0] == "Evergate"
    assert len(response.json()["matches"]) == 1

def test_search_no_match():
    response = client.get('/search/xxxxxxx')
    assert response.status_code == 404
    assert response.json() == {"message": "Game not found"}

def test_search_in_graph():
    response = client.get('/')
    response = client.get('/search/ku')
    assert response.status_code == 200
    assert response.json()["match_in_graph"][0] == "Sengoku Rance"
    assert response.json()["match_in_graph"][1] == "Carol Vorderman's Sudoku"
    assert len(response.json()["match_in_graph"]) == 2

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
    
# test if a detailpage is shown
def test_detailpage():
    response = client.get('/detail/Evergate')
    assert response.status_code == 200
    assert response.json() == detailpage_content("Evergate")

def test_detailpage_no_input():
    response = client.get('/detail/xxxxxxx')
    assert response.status_code == 404
    assert response.json() == {"message": "Game not found"}