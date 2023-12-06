
from passlib.context import CryptContext
from .auth_handler import signJWT
from ....models.user import User
import time
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def auth(user_schema,db): 
    user = db.query(User).filter(User.username==user_schema.username).first()
    if not  user:
        return {
            "error": "The username or password are invalid!"
        }
    

    if verify_password(user_schema.password,user.password):
        user.last_login = datetime.fromtimestamp(time.time())
        db.add(user)
        db.commit()
        db.refresh(user)
        return signJWT(user)
    return {
        "error": "The username or password are invalid!"
    }


def verify_password(password,hasd_password):
    if pwd_context.verify(password,hasd_password):
        return True
    return False


def hash_password(password)->str:
    return pwd_context.hash(password)
