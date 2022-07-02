setup-test-db:
	docker run --name test-db \
	-e POSTGRES_USER=test \
	-e POSTGRES_PASSWORD=test \
	-e POSTGRES_DB=test \
	-p 5433:5432 \
	-d \
	postgres:latest

cleanup-test-db:
	docker rm -f test-db

migrate:
	@python3 -m main -p examples/ -d postgres://test:test@localhost:5433/test
