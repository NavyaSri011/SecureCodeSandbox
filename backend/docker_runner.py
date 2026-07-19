import os
import subprocess
import time

from config import (
    EXECUTION_TIMEOUT,
    MEMORY_LIMIT,
    CPU_LIMIT,
    TEMP_FOLDER,
    SUPPORTED_LANGUAGES,
)


def run_command(filename, language, user_input):

    temp_path = os.path.abspath(TEMP_FOLDER)

    if language not in SUPPORTED_LANGUAGES:
        return {
            "output": "",
            "error": "Unsupported language"
        }

    image = SUPPORTED_LANGUAGES[language]["image"]

    # Language execution commands
    if language == "python":

        command = [
            "python",
            filename
        ]

    elif language == "c":

        name = os.path.splitext(filename)[0]

        command = [
            "sh",
            "-c",
            f"gcc {filename} -o {name} && ./{name}"
        ]

    elif language == "cpp":

        name = os.path.splitext(filename)[0]

        command = [
            "sh",
            "-c",
            f"g++ {filename} -o {name} && ./{name}"
        ]

    elif language == "java":

        name = os.path.splitext(filename)[0]

        command = [
            "sh",
            "-c",
            f"javac {filename} && java {name}"
        ]

    else:

        return {
            "output": "",
            "error": "Unsupported language"
        }

    # Docker sandbox command
    docker_command = [

        "docker",
        "run",

        "--rm",

        "-i",

        # Disable internet
        "--network",
        "none",

        # Memory restriction
        "--memory",
        MEMORY_LIMIT,

        # CPU restriction
        "--cpus",
        CPU_LIMIT,

        # Process restriction
        "--pids-limit",
        "50",

        # Mount temporary code folder
        "-v",
        f"{temp_path}:/app",

        "-w",
        "/app",

        image

    ] + command

    try:

        start = time.perf_counter()

        result = subprocess.run(
            docker_command,
            input=user_input,
            capture_output=True,
            text=True,
            timeout=EXECUTION_TIMEOUT
        )

        end = time.perf_counter()

        return {

            "output": result.stdout,

            "error": result.stderr,

            "execution_time": round(
                end - start,
                4
            ),

            "exit_code": result.returncode

        }

    except subprocess.TimeoutExpired:

        return {

            "output": "",

            "error": "Execution timed out"

        }

    except FileNotFoundError:

        return {

            "output": "",

            "error": "Docker is not installed or not running"

        }

    except Exception as e:

        return {

            "output": "",

            "error": str(e)

        }
