from fastapi import FastAPI
from .api import router as api_router
import os

app = FastAPI(title='KYC backend demo')
app.include_router(api_router, prefix='/api')

os.makedirs(os.path.join(os.path.dirname(__file__), 'audit'), exist_ok=True)
