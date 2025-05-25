from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON file once at startup
json_path = os.path.join(os.path.dirname(__file__), "students.json")
with open(json_path) as f:
    student_marks = json.load(f)

@app.get("/")
def root():
    return {"message": "Use /api?name=Alice&name=Bob to get marks"}

@app.get("/api")
def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_marks.get(name, None) for name in names]
    return {"marks": marks}
