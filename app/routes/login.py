from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from app.storage.db import get_db, find_user_by_email
from app.auth import create_access_token
from app.models.schemas import LoginRequest

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login")
def login(body: LoginRequest, db=Depends(get_db)):
    # 1. Find user
    user = find_user_by_email(db, body.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    # 2. Verify password
    if not pwd_context.verify(body.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    # 3. Return token
    token = create_access_token(email=user["email"])
    return {"access_token": token, "token_type": "bearer"}