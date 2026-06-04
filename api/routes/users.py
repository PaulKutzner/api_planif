from fastapi import APIRouter, HTTPException 

from api.db import SessionLocal 
from api.models.user import User
from api.schemas.user import (UserCreate, UserResponse) 
from api.services.password import hash_password 


router = APIRouter()

@router.post("/users",
             response_model=UserResponse)

def create_user(data: UserCreate):
    database= SessionLocal()

    existing_user = (
        database.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email déjà existant"

        )
    hashed =hash_password(data.password)
    new_user = User(
        email=data.email,
        hashed_password=hashed
    )

    database.add(new_user)

    database.commit()

    database.refresh(new_user)

    return new_user