
from fastapi import FastAPI
from app.router.router import router

app = FastAPI(title="Weather API", version="1.0")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)