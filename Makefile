up-build:
	docker compose -f docker-compose.yaml up -d --build
up:
	docker compose -f docker-compose.yaml up -d
down:
	docker compose -f docker-compose.yaml down
