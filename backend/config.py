TEMP_FOLDER = "temp"

EXECUTION_TIMEOUT = 5

DOCKER_IMAGE = "python:3.12-slim"

MEMORY_LIMIT = "128m"

CPU_LIMIT = "0.5"

SUPPORTED_LANGUAGES = {
    "python": {
        "extension": "py",
        "command": "python",
        "image": DOCKER_IMAGE
    }
}
