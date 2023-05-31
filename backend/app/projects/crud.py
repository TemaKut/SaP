from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.base import get_async_session
from app.projects.models import Project
from app.projects.schemas import ProjectCreate


class ProjectsCRUD():
    """ CRUD операции в бд для проектов """

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        """ Инициализация объекта класса. """
        self.session = session

    async def create_project(self, data: ProjectCreate) -> Project:
        """ Создать проект """
        new_project = Project(**data.dict())

        self.session.add(new_project)
        await self.session.commit()
        await self.session.refresh(new_project)

        return new_project
