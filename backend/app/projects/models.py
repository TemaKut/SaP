import os

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

from app.database.base import Base
from app.settings import STATIC_BASE_URI


class Project(Base):
    """ Модель проекта в БД. """
    __tablename__ = 'projects'

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        comment='Id проекта'
    )
    title = sa.Column(
        sa.String(200),
        nullable=False,
        comment='Краткое описание проекта.'
    )
    description = sa.Column(
        sa.Text,
        nullable=False,
        comment='Подробное описание проекта'
    )
    photo_uris = sa.Column(
        JSONB,
        nullable=False,
        default=[
            os.path.join(STATIC_BASE_URI, 'projects', 'DefaultUserLogo.png'),
        ],
        comment='Список ссылок на фотографии проекта'
    )

    def __repr__(self) -> str:
        """ Строчное представление проекта. """

        return f'{self.__class__.__name__}<id={self.id}>'
