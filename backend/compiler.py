from config import SUPPORTED_LANGUAGES


def get_execution_details(language, filename):

    if language not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported language")

    return {
        "image": SUPPORTED_LANGUAGES[language]["image"],
        "command": SUPPORTED_LANGUAGES[language]["command"],
        "filename": filename
    }
