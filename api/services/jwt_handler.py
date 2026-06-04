from jose import jwt 
from datetime import datetime, timedelta 
from api.config import CLE_SECRETE 

ALGO= "HS256"

def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = (
        datetime.utcnow() + 
        timedelta(hours=1)
    )

    token = jwt.encode(
        payload,
        CLE_SECRETE,
        algorithm=ALGO
    )
    return token
