from fastapi.testclient import TestClient
from db_wrapper import detailpage_content, search_query
from main import app
import json

client = TestClient(app)

# todo: test the root graph
def test_startpage():
    response = client.get('/')
    assert response.status_code == 200
    assert len(response.json()["data"]) == 38
    assert response.json()["data"]["1989"] == ["Denaris"]
    
# test if a detailpage is shown
def test_detailpage():
    response = client.get('/detail/Evergate')
    assert response.status_code == 200
    assert response.json() == detailpage_content("Evergate")

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
    