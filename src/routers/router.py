from fastapi import APIRouter
from controllers.auth import register, login, get_users

router = APIRouter()

router.post("/register")(register)
router.post("/login")(login)
router.get("/")(get_users)