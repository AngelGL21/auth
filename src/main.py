from fastapi import FastAPI
from routers.router import router as auth_router

app = FastAPI()
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)