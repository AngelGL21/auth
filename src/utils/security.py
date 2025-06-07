import bcrypt
import logging
import re

# Configurar logging
logging.basicConfig(
    filename='auth_events.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(name)s] %(message)s'
)
logger = logging.getLogger(__name__)

def validate_username(username: str) -> bool:
    pattern = r"^[a-zA-Z0-9_]{3,30}$"
    return bool(re.match(pattern, username))

def log_login_attempt(ip: str, username: str, status: str):
    logger.info(
        f"Login attempt - IP: {ip} | User: {username} | Status: {status}"
    )

#  funciones para encriptar y verificar
def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password)
