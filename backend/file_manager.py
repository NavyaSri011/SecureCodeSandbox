import os
import uuid
from config import TEMP_FOLDER


def create_temp_file(code: str, extension: str):
    os.makedirs(TEMP_FOLDER, exist_ok=True)

    filename = f"{uuid.uuid4()}.{extension}"

    file_path = os.path.join(TEMP_FOLDER, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code)

    return file_path, filename


def delete_temp_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
