import os
import subprocess
import time
from config import (
    DOCKER_IMAGE,
    EXECUTION_TIMEOUT,
    MEMORY_LIMIT,
    CPU_LIMIT,
    TEMP_FOLDER,
)


def run_command(filename, user_input):
    temp_path = os.path.abspath(TEMP_FOLDER)

    command = [
        "docker",
        "run",
        "--rm",
        "-i",

        "--network", "none",

        "--memory", MEMORY_LIMIT,

        "--cpus", CPU_LIMIT,

        "-v", f"{temp_path}:/app",

        "-w", "/app",

        DOCKER_IMAGE,

        "python",

        filename,
    ]

    try:
        start_time = time.perf_counter()
        result = subprocess.run(
            command,
            input=user_input + "\n",
            capture_output=True,
            text=True,
            timeout=EXECUTION_TIMEOUT,
        )

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return {
            "output": result.stdout,
            "error": result.stderr,
            "execution_time": round(execution_time, 4),
            "exit_code": result.returncode
        }

    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "error": "Execution timed out",
        }
