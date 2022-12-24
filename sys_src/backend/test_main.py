from fastapi.testclient import TestClient
from db_wrapper import detailpage_content, search_query
from filter_lists import get_data
from main import app
import json

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
    assert "The Last of Us" in response.json()["2013"]

# test if a search request with multiple games are correct
def test_search():
    response = client.get('/search/eve')
    assert response.status_code == 200
    dump_test = json.dumps(search_query("eve"))
    assert dump_test in str(response.json())
    
# test if it's only a single game with the searched name
def test_search_single():
    response = client.get('/search/Evergate')
    assert response.status_code == 200
    assert response.json() == detailpage_content("Evergate")

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