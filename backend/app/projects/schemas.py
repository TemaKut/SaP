from pydantic import BaseModel


class ProjectRepresentation(BaseModel):
    """ Данные проекта для response. """

    id: int
    title: str
    description: str
    photo_uris: list[str]

    class Config:

        orm_mode = True


class ProjectCreate(BaseModel):
    """ Данные для создания проекта. """

    title: str = 'Sometitle'
    description: str = 'SomeDescr'
    photo_uris: list[str] = None
