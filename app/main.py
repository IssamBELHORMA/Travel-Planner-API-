from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, login, plan

app = FastAPI(title="Travel Planner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(login.router)
app.include_router(plan.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}