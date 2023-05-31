from fastapi import APIRouter, Body, Depends

from app.projects.crud import ProjectsCRUD
from app.projects.schemas import ProjectCreate, ProjectRepresentation


projects_router = APIRouter(
    prefix='/projects',
    tags=['Проекты']
)


@projects_router.post(
    '/',
    response_model=ProjectRepresentation,
)
async def project_create(
    data: ProjectCreate = Body(),
    crud: ProjectsCRUD = Depends(),
):
    """ Создать проект. """

    return await crud.create_project(data)
