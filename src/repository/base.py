from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from typing import TypeVar, Type, Optional

from database import Base
from repository.enum import SynchronizeSessionEnum


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepo:
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def update_by_id(self,
                           id: int,
                           params: dict,
                           synchronize_session: SynchronizeSessionEnum = False,
                           ) -> None:
        query = (
            update(self.model)
            .where(self.model.id == id)
            .values(**params)
            .execution_options(synchronize_session=synchronize_session)
        )
        await self.session.execute(query)

    async def delete(self, model: ModelType) -> None:
        await self.session.selete(model)

    async def delete_by_id(
        self,
        id: int,
        synchronize_session: SynchronizeSessionEnum = False,
    ) -> None:
        query = (
            delete(self.model)
            .where(self.model.id == id)
            .execution_options(synchronize_session=synchronize_session)
        )
        await self.session.execute(query)

    async def save(self, model: ModelType) -> ModelType:
        saved = await self.session.add(model)
        return saved