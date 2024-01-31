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

| Kommando           | Beschreibung                                     |
|--------------------|--------------------------------------------------|
| `python -m uvicorn main:app` | Startet das Backend.|
| `pip freeze > requirements.txt` | Erstellt/Aktulaisiert die Requirements Textdatei.|
| `python -m pytest --cov -v --cov-report term-missing --cov-branch` | Führt Unittests für alle Dateien durch.|
| `python -m --cov main --cov-branch --cov-report term-missing` | Führt Unittest für main.py durch.|

Im Frontend stehen folgende Kommandos zur Verfügung:

| Kommando           | Beschreibung                         |
|--------------------|--------------------------------------|
| `npm run build`    | Baut das Frontend.                   |
| `npm run start`    | Baut das Frontend und startet es.    |
| `npm run test`     | Führt die Tests aus.                 |
| `npm run coverage` | Erstellt einen Code-Coverage Report. |


## Docker 

Das System lässt sich mit `docker compose up` starten.

## Tech Stack
cyberlytics/SGDb is built on the following main stack:

- <img width='25' height='25' src='https://img.stackshare.io/service/993/pUBY5pVj.png' alt='Python'/> [Python](https://www.python.org) – Languages
- <img width='25' height='25' src='https://img.stackshare.io/service/1011/n1JRsFeB_400x400.png' alt='Node.js'/> [Node.js](http://nodejs.org/) – Frameworks (Full Stack)
- <img width='25' height='25' src='https://img.stackshare.io/service/1209/javascript.jpeg' alt='JavaScript'/> [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) – Languages
- <img width='25' height='25' src='https://img.stackshare.io/service/1612/bynNY5dJ.jpg' alt='TypeScript'/> [TypeScript](http://www.typescriptlang.org) – Languages
- <img width='25' height='25' src='https://img.stackshare.io/service/2202/72d087642cfce6fef6f2dabec5bf49e8_400x400.png' alt='Autoprefixer'/> [Autoprefixer](https://github.com/postcss/autoprefixer) – CSS Pre-processors / Extensions
- <img width='25' height='25' src='https://img.stackshare.io/service/3339/rlFcjEdI.png' alt='PostCSS'/> [PostCSS](https://github.com/postcss/postcss) – CSS Pre-processors / Extensions
- <img width='25' height='25' src='https://img.stackshare.io/service/4586/Lu99Qe0Z_400x400.png' alt='pytest'/> [pytest](http://pytest.org/latest/) – Testing Frameworks
- <img width='25' height='25' src='https://img.stackshare.io/service/6113/7exmJEg4_400x400.png' alt='Svelte'/> [Svelte](https://svelte.technology/) – Javascript UI Libraries
- <img width='25' height='25' src='https://img.stackshare.io/service/7054/preview.jpeg' alt='jsdom'/> [jsdom](https://github.com/jsdom/jsdom) – Headless Browsers
- <img width='25' height='25' src='https://img.stackshare.io/service/7071/MrEYkPFd_400x400.jpg' alt='Dgraph'/> [Dgraph](https://dgraph.io/) – Graph Databases
- <img width='25' height='25' src='https://img.stackshare.io/service/8158/default_660b7c41c3ba489cb581eec89c04655404258c19.png' alt='Tailwind CSS'/> [Tailwind CSS](https://tailwindcss.com) – Front-End Frameworks
- <img width='25' height='25' src='https://img.stackshare.io/service/11246/favicon-image-large.png' alt='Refinery'/> [Refinery](https://www.refinery.io) – API Tools
- <img width='25' height='25' src='https://img.stackshare.io/service/21547/default_1aeac791cde11ff66cc0b20dcc6144eeb185c905.png' alt='Vite'/> [Vite](https://vitejs.dev/) – JS Build Tools / JS Task Runners
- <img width='25' height='25' src='https://img.stackshare.io/service/25014/default_f6ff39141b468e832d1bc59fc98a060df604d44d.png' alt='FastAPI'/> [FastAPI](https://fastapi.tiangolo.com/) – Microframeworks (Backend)
- <img width='25' height='25' src='https://img.stackshare.io/service/586/n4u37v9t_400x400.png' alt='Docker'/> [Docker](https://www.docker.com/) – Virtual Machine Platforms & Containers

Full tech stack [here](/techstack.md)
