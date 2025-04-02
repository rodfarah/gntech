# Start the containers
up:
	docker compose up --build

# Stop the containers
down:
	docker compose down

# Build the Docker image for the backend service
build:
	docker compose build
