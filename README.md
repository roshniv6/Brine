# Brine
Senior Infra Engineer in Brine

# Your Project

## Instructions

1. Clone the repository.
2. Build the Docker image:
    ```bash
    docker build -t your_project .
    ```
3. Run the Docker container:
    ```bash
    docker run your_project
    ```
4. Run tests:
    ```bash
    docker build -t your_project_test -f Dockerfile.test .
    docker run your_project_test
    ```

## Explanation

- `main.py` contains the main logic for reading orders and performing the required computations.
- `test_main.py` contains unit tests for the main functions.
- `Dockerfile` is used to create a Docker image for the main application.
- `requirements.txt` lists the Python dependencies.
- `README.md` provides instructions for running the application and tests.

