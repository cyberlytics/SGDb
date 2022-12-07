.DEFAULT_GOAL := dev-start

# Preload the database with RDF data
dev-preload:
	cd ./preload && docker compose up --build -d

# Build the system for development
dev-build:
	docker compose build

# Start the system in development mode
dev-start:
	docker compose up

# Build and start the system in development mode
dev-build-start:
	docker compose up --build

# Stop the system
dev-stop:
	docker compose down