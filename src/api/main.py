"""MasLeads API"""

# FastAPI
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Routers
from src.api.routers import elements

app = FastAPI(
    title='📧 MasLeads Elements Microservice',
    description='This is a super cool api for consult and handle the MasLeads Elements',
)

app.include_router(elements.router)

@app.get('/')
def index():
    return RedirectResponse('/docs')
