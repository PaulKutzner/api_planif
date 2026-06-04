from fastapi import APIRouter, HTTPException 
from api.db import SessionLocal 
from api.models.user import User 
from api.schemas.user import LoginData 

from api.services.password import verify_password

from api.services.jwt_handler import create_access_token

router = APIRouter()

@router.post("/login")

def login(data: LoginData):
    database=SessionLocal()

    user = (database.query(User)
            .filter(User.email == data.email)
            .first()
            )
    
    if not user: 
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    valid_password= verify_password(
        data.password,
        user.hashed_password
    )    

    if not valid_password: 
            raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "sub" : user.email
    })

    return {
         "access_token": token, 
         "token_type": "bearer"
    }