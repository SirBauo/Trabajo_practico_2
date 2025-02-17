from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

api = FastAPI(
    title="MLOPS first API",
    description="MLOPS first API",
    version="0.0.1"
)

