from fastapi import APIRouter
from controllers.auth import register, login, get_users, simulate_error, change_password, refresh_token, evaluar_tecnologias
from controllers.monitor import obtener_errores, obtener_causas, obtener_acciones

router = APIRouter()

auth_router = APIRouter(prefix="/auth", tags=["Autenticación"])
auth_router.post("/register")(register)
auth_router.post("/login")(login)
auth_router.post("/change_password")(change_password)
auth_router.get("/")(get_users)
auth_router.get("/refresh_token")(refresh_token)

# Rutas de monitoreo
monitor_router = APIRouter(prefix="/admin", tags=["Monitoreo"])
monitor_router.get("/errores")(obtener_errores)
monitor_router.get("/causas")(obtener_causas)
monitor_router.get("/acciones")(obtener_acciones)
monitor_router.post("/simulate_error")(simulate_error)

tecnologia_router = APIRouter(prefix="/tecnologia", tags=["Tecnología"])
tecnologia_router.get("/evaluation")(evaluar_tecnologias)


# Incluye los routers en el router principal
router.include_router(auth_router)
router.include_router(monitor_router)
router.include_router(tecnologia_router)
