from fastapi import FastAPI
from models import CodeRequest
from executor import execute
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Secure Code Sandbox"
    }


@app.post("/run")
def run_code(request: CodeRequest):
    return execute(request)
