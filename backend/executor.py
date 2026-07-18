from file_manager import create_temp_file, delete_temp_file
from docker_runner import run_command
from config import SUPPORTED_LANGUAGES


def execute(request):

    # Check if the language is supported
    if request.language not in SUPPORTED_LANGUAGES:
        return {
            "error": "Unsupported language"
        }

    # Get the file extension for the selected language
    extension = SUPPORTED_LANGUAGES[request.language]["extension"]

    # Create a temporary source code file
    file_path, filename = create_temp_file(
        request.code,
        extension
    )

    try:
        # Execute the file inside Docker
        result = run_command(filename, request.input)

        return result

    finally:
        # Delete the temporary file after execution
        delete_temp_file(file_path)
