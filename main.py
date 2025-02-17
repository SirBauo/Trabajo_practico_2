from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="MLOPS Trabajo practico 2",
    description="MLOPS Trabajo practico 2",
    version="0.0.1"
)
users = []

@app.post("/users/")
def create_user(user: dict):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}
