from datetime import datetime, timedelta
from jose import JWTError, jwt

# Clave secreta (cámbiala en producción)
SECRET_KEY = "mi_clave_secreta"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 1

def crear_token(username: str):
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    payload = {
        "sub": username,
        "exp": expiration
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str, allow_expired: bool = False):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_exp": not allow_expired})
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        if allow_expired:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_exp": False})
            return payload.get("sub")
        return None
    except jwt.InvalidTokenError:
        return None
