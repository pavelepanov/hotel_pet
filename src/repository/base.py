from sqlalchemy import update, delete

from typing import TypeVar, Type

from database import Base, async_session_maker


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepo:
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def update_by_id(self,
                           id: int,
                           params: dict,
                           ) -> None:
        query = (
            update(self.model)
            .where(self.model.id == id)
            .values(**params)
        )
        with async_session_maker() as session:
            await session.execute(query)
            await session.commit()

    async def delete(self, model: ModelType) -> None:
        with async_session_maker() as session:
            await session.delete(model)
            await session.commit()

    async def delete_by_id(
        self,
        id: int,
    ) -> None:
        query = (
            delete(self.model)
            .where(self.model.id == id)
        )
        with async_session_maker() as session:
            await session.execute(query)
            await session.commit()

    async def save(self, model: ModelType) -> ModelType:
        saved = await self.session.add(model)
        return saved