from sqlalchemy import select, update, delete

from typing import TypeVar, Type

from database import Base


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
        await self.session.execute(query)
        await self.session.commit()

    async def delete(self, model: ModelType) -> None:
        await self.session.selete(model)

    async def delete_by_id(
        self,
        id: int,
    ) -> None:
        query = (
            delete(self.model)
            .where(self.model.id == id)
        )
        await self.session.execute(query)

    async def save(self, model: ModelType) -> ModelType:
        saved = await self.session.add(model)
        return saved