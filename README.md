# sunfish-backend

Sunfish Backend

1. Clone the repo:
    git clone https://github.com/timuy/sunfish-backend.git
2. Install Docker Desktop (https://www.docker.com/products/docker-desktop/)
3. cd to sunfish-backend
4. Run docker-compose to spin up Docker locally
    docker-compose up --build -d
5. Use IDE of your choice to connect to Docker container or via command line: docker exec -it sunfish-backend bash
6. Once in the Docker container, please bring up uvicorn to bring up the REST API
    $HOME/.local/bin/poetry run uvicorn src.app:app --reload --host 0.0.0.0 --port 8080
7. URL for docs:
    swagger:  http://localhost:8080/docs
    redoc:  http://localhost:8080/redoc
    openapi.json:  http://localhost:8080/openapi.json


Implementation

1. Use FastAPI as framework to run REST API
2. Use uvicorn as server for the REST API
    $HOME/.local/bin/poetry run uvicorn src.app:app --reload --host 0.0.0.0 --port 8080

3. The URL of the REST API is:  http://localhost:8080/ivf/estimator

4. Used ruff for linting.
    $HOME/.local/bin/poetry run python -m ruff check

5. Run the following command for unit tests:

    $HOME/.local/bin/poetry run python -m pytest tests -s -vv
