import datetime
from typing import Annotated
from pydantic import FilePath, Json
from sqlalchemy import String, ForeignKey, text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
str_32 = Annotated[str, mapped_column(String(32))]


class Base(DeclarativeBase):
    pass


class CategoryDish(Base):
    __tablename__ = 'category_dish'

    id: Mapped[intpk]
    name: Mapped[str_32]
    slug: Mapped[str_32]


class RecipeDish(Base):
    __tablename__ = 'recipe_dish'

    id: Mapped[intpk]
    name: Mapped[str_32]
    slug: Mapped[str_32]
    category: Mapped[str] = mapped_column(ForeignKey('category_dish.name'))
    description: Mapped[str | None]
    ingredients: Mapped[Json | None]
    recipe: Mapped[str | None]
    published: Mapped[datetime.datetime] = mapped_column(
        server_default=text('TIMEZONE("utc", now())'))
    image: Mapped[FilePath]
    author: Mapped[str]
