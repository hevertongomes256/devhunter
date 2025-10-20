from fastapi import APIRouter

from api.v1.endpoints import vagas
from api.v1.endpoints import usuario


api_router = APIRouter()

api_router.include_router(vagas.router, prefix='/vagas', tags=['vagas'])
api_router.include_router(
    usuario.router, prefix='/usuarios', tags=['usuarios'])
