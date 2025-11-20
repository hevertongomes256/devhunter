
from httpx import AsyncClient
from pytest_asyncio import fixture as asyncio_fixture
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from core.deps import get_session
from core.configs import settings


TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)


TestSessionLocal = sessionmaker(
    test_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


@asyncio_fixture
async def prepare_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)


@asyncio_fixture
async def db_session():
    async with TestSessionLocal() as session:
        yield session


@asyncio_fixture
async def client(db_session):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_session] = override_get_db

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
