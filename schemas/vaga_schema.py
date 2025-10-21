from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class VagaSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url: HttpUrl
    data_criacao:  Optional[datetime]
    disponivel: bool
    usuario_id: Optional[int]

    class Config:
        orm_mode = True
