from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.storage.db import get_db, get_activities_by_city
from app.dependencies import get_current_user
from app.models.schemas import PlanRequest
from app.services.weather import get_weather

router = APIRouter()

@router.post("/plan")
def get_travel_plan(body: PlanRequest, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Récupération des activités directement depuis MySQL
    activities = get_activities_by_city(db, body.city)

    try:
        weather = get_weather(body.city)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Weather service unavailable: {exc}")

    return {
        "user": current_user["email"],
        "city": body.city,
        "weather": weather,
        "activities": activities
    }