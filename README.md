# SGDb: Semantic Game Database

SGDb ist eine webbasierte Anwendung mit einer Graphen-basierten Suche von Videospielen

## Aufbau

Das Monorepo gliedert sich in folgende fünf Unterordner 
- `backend` - Backend der Anwendung mit FastAPI
- `frontend` - Frontend der Anwendung mit Svelte
- `database` - Datenbank der Anwendung mit GraphDB
- `refine` - Überführung der semi-strukturierten Daten RDF-Triples mit OntoText Refine
- `preload`- Lädt RDF-Triples in die Datenbank (nur wenn die Datenbank offline ist) 

## Entwicklungsumgebung

Die Abhängigkeiten können in beiden Teilprojekten wie folgt installiert werden:

```bash
cd sys_src/backend # Wechsel ins Backend-Teilprojekt-Verzeichnis
pip install # Installation der Abhängigkeiten

cd sys_src/frontend # Wechsel ins Frontend-Teilprojekt-Verzeichnis
npm install # Installation der Abhängigkeiten
```

Im Backend stehen folgende Kommandos zur Verfügung:

| Kommando           | Beschreibung         |
|--------------------|----------------------|
| `uvicorn main:app` | Startet das Backend. |

Im Frontend stehen folgende Kommandos zur Verfügung:

| Kommando           | Beschreibung                         |
|--------------------|--------------------------------------|
| `npm run build`    | Baut das Frontend.                   |
| `npm run start`    | Baut das Frontend und startet es.    |
| `npm run test`     | Führt die Tests aus.                 |
| `npm run coverage` | Erstellt einen Code-Coverage Report. |


## Docker 

Das System lässt sich mit `docker compose up` starten.