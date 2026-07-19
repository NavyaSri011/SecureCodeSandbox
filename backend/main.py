from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import CodeRequest
from executor import execute
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Secure Code Sandbox"
    }


@app.post("/run")
def run_code(request: CodeRequest):
    return execute(request)
