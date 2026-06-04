from fastapi import APIRouter, HTTPException, status, Depends
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from app.storage.db import get_db, find_user_by_email, create_user
from app.models.schemas import UserCreate

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/users", status_code=201)
def register(body: UserCreate, db=Depends(get_db)):
    # 1. Check if email already exists
    if find_user_by_email(db, body.email):
        raise HTTPException(status_code=409, detail="Email already registered.")

    # 2. Hash the password
    hashed = pwd_context.hash(body.password)

    # 3. Create the user in the database
    try:
        new_user = create_user(db, body.email, hashed)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Email already registered.")

    # 4. Return only safe fields (never return the password)
    return {"id": new_user["id"], "email": new_user["email"]}