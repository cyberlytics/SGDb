from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def startpage():
    return{"message": "Startpage"}

games = [
    {"name": "CS:GO", "preis": 0, "genre": "Shooter"},
    {"name": "Dota", "preis": 0, "genre": "Moba"},
    {"name": "Need for Speed", "preis": 50, "genre": "Rennspiel"},
]

@app.get("/games")
def search(search: str):
    return next(item for item in games if item["name"] == search)
