from fastapi.testclient import TestClient
from db_wrapper import query_all, detailpage_content, search_query
from main import app

client = TestClient(app)
graph = query_all()

# todo: test the root graph
def test_startpage():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "rootgraph"}
    
# test if a detailpage is shown
def test_detailpage():
    response = client.get('/detail/Evergate')
    assert response.status_code == 200
    assert response.json() == {"message": detailpage_content(graph, "Evergate")}

# test if a search request with multiple games are correct
def test_search():
    response = client.get('/search/eve')
    assert response.status_code == 200
    assert response.json() == {"message": search_query(graph, "eve")}
    
# test if it's only a single game with the searched name
def test_search_single():
    response = client.get('/search/Evergate')
    assert response.status_code == 200
    assert response.json() == {"message": detailpage_content(graph, "Evergate")}

# test if there is no title for search
def test_search_with_no_content():
    response = client.get('/search/')
    assert response.status_code == 200
    assert response.json() == {"message": "please enter a title for search"}
    