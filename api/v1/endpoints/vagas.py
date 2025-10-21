from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.vaga_model import VagaModel
from models.usuario_model import UsuarioModel
from schemas.vaga_schema import VagaSchema
from core.deps import get_session, get_current_user


router = APIRouter()


# POST Vaga
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=VagaSchema)
async def post_vaga(vaga: VagaSchema, usuario_logado: UsuarioModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    nova_vaga: VagaModel = VagaModel(
        titulo=vaga.titulo,
        descricao=vaga.descricao,
        url=vaga.url,
        disponivel=vaga.disponivel,
        usuario_id=usuario_logado.id
    )

    db.add(nova_vaga)
    await db.commit()
    await db.refresh(nova_vaga)

    return nova_vaga


# GET Vagas
@router.get('/', response_model=List[VagaSchema])
async def get_vagas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VagaModel)
        result = await session.execute(query)
        vegas: List[VagaModel] = result.scalars().unique().all()

        return vegas


# GET Vaga
@router.get('/{vaga_id}', response_model=VagaSchema, status_code=status.HTTP_200_OK)
async def get_vaga(vaga_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VagaModel).filter(VagaModel.id == vaga_id)
        result = await session.execute(query)
        vaga: VagaModel = result.scalars().unique().one_or_none()

        if vaga:
            return vaga
        else:
            raise HTTPException(detail='Vaga não encontrada',
                                status_code=status.HTTP_404_NOT_FOUND)


# PUT Vaga
@router.put('/{vaga_id}', response_model=VagaSchema, status_code=status.HTTP_200_OK)
async def put_vaga(vaga_id: int, vaga: VagaSchema, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(VagaModel).filter(VagaModel.id == vaga_id)
        result = await session.execute(query)
        vaga_up: VagaModel = result.scalars().unique().one_or_none()

        if not vaga_up:
            raise HTTPException(detail='Vaga não encontrada', status_code=status.HTTP_404_NOT_FOUND)

        dados_para_atualizar_vaga = vaga.dict(exclude_unset=True)

        for campo, valor in dados_para_atualizar_vaga.items():
            setattr(vaga_up, campo, valor)

        if usuario_logado.id != vaga_up.usuario_id:
            vaga_up.usuario_id = usuario_logado.id

        await session.commit()
        await session.refresh(vaga_up)

        return vaga_up


# DELETE Artigo
@router.delete('/{vaga_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_vaga(vaga_id: int, db: AsyncSession = Depends(get_session), usuario_logado: UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(VagaModel).filter(VagaModel.id == vaga_id).filter(
            VagaModel.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        vaga_del: VagaModel = result.scalars().unique().one_or_none()

        if vaga_del:
            await session.delete(vaga_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Vaga não encontrada',
                                status_code=status.HTTP_404_NOT_FOUND)
