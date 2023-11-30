import datetime
from typing import Annotated
from sqlalchemy import JSON, String, ForeignKey, Text, text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
str_name = Annotated[str, mapped_column(String(32), unique=True)]
str_slug = Annotated[str, mapped_column(String(32), unique=True)]


class Base(DeclarativeBase):
    pass


class CategoryDish(Base):
    __tablename__ = 'category_dish'

    id: Mapped[intpk]
    name: Mapped[str_name]
    slug: Mapped[str_slug]


class RecipeDish(Base):
    __tablename__ = 'recipe_dish'

    id: Mapped[intpk]
    name: Mapped[str_name]
    slug: Mapped[str_slug]
    category: Mapped[str] = mapped_column(ForeignKey('category_dish.name'))
    description: Mapped[str | None] = mapped_column(String(1024))
    ingredients: Mapped[dict] = mapped_column(type_=JSON)
    recipe: Mapped[str | None] = mapped_column(type_=Text)
    published: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"))
    image: Mapped[str]
    author: Mapped[str]
