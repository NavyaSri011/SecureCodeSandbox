TEMP_FOLDER = "temp"

EXECUTION_TIMEOUT = 5

DOCKER_IMAGE = "python:3.12-slim"

MEMORY_LIMIT = "128m"

CPU_LIMIT = "0.5"

SUPPORTED_LANGUAGES = {
    "python": {
        "extension": "py",
        "command": "python",
        "image": "python:3.12-slim"
    },

    "c": {
        "extension": "c",
        "command": "gcc",
        "image": "gcc:latest"
    },

    "cpp": {
        "extension": "cpp",
        "command": "g++",
        "image": "gcc:latest"
    },

    "java": {
        "extension": "java",
        "command": "java",
        "image": "eclipse-temurin:21"
    }
}
