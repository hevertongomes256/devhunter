from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from core.configs import settings


class VagaModel(settings.DBBaseModel):
    __tablename__ = 'vagas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(256), nullable=False)
    descricao = Column(String(256), nullable=False)
    url = Column(String(256))
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    disponivel = Column(Boolean, default=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    criador = relationship(
        "UsuarioModel",
        back_populates='artigos',
        lazy='joined'
    )
