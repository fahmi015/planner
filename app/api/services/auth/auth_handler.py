import time
from datetime import datetime
from typing import Dict
import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str,user):
    return {
        "user":user,
        "access_token":token
    }


def signJWT(user) -> Dict[str, str]:
    payload = {
        "user_id": user.id,
        "expires": time.time() + 15 * 60 * 1000,
        "created_at":time.time()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token,user)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
    
    
def expirationDataJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        expiretion_date=datetime.fromtimestamp(decoded_token["created_at"])
        return expiretion_date
    except:
        return time.time()
