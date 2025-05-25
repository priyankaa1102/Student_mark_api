from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Sample data (replace with your actual dataset)
data = {
    "Alice": 78,
    "Bob": 92,
    "Charlie": 65,
    # Add all 100 students here
}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks = [data.get(n, None) for n in name]
    return JSONResponse(content={"marks": marks})
