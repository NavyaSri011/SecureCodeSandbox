import os

from file_manager import create_temp_file, delete_temp_file
from docker_runner import run_command
from config import SUPPORTED_LANGUAGES


def execute(request):

    # Check if language is supported
    if request.language not in SUPPORTED_LANGUAGES:
        return {
            "error": "Unsupported language"
        }

    extension = SUPPORTED_LANGUAGES[request.language]["extension"]

    # Java requires Main.java
    if request.language == "java":

        file_path, filename = create_temp_file(
            request.code,
            extension
        )

        new_path = os.path.join(
            os.path.dirname(file_path),
            "Main.java"
        )

        os.rename(file_path, new_path)

        file_path = new_path
        filename = "Main.java"

    else:

        file_path, filename = create_temp_file(
            request.code,
            extension
        )

    try:
        result = run_command(
            filename,
            request.language,
            request.input
        )

        return result

    finally:
        delete_temp_file(file_path)
