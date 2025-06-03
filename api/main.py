from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import task, done

app = FastAPI()

app.include_router(task.router)
app.include_router(done.router)

@app.get("/")
async def root():
    return {"message": "Todo API"}

