from fastapi import FastAPI, HTTPException
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the CRM Leads API"}
