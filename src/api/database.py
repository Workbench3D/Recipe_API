import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from api.models import Base, CategoryDish, RecipeDish


engine = create_engine(url=os.getenv('DATABASE_URL'), echo=True,)


session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class RecipeORM:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_test_data():
        with session_factory() as session:
            category_first = CategoryDish(name='Первое', slug='first')
            category_second = CategoryDish(name='Второе', slug='second')

            recipe_borsch = RecipeDish(
                name='Борщ',
                slug='borsch',
                category='Первое',
                description='Lorem Ipsum',
                ingredients={'Test': 100, 'Вода': 10, 'Мясо': 2},
                recipe='Lorem Ipsum',
                image='filepath',
                author='john',
            )
            recipe_paste = RecipeDish(
                name='Паста',
                slug='paste',
                category='Второе',
                description='Lorem Ipsum',
                ingredients={'Макароны': 100, 'Соль': 10, 'Масло': 4},
                recipe='Lorem Ipsum',
                image='filepath',
                author='john',
            )
            recipe_cutlets = RecipeDish(
                name='Котлеты',
                slug='cutlets',
                category='Второе',
                description='Lorem Ipsum',
                ingredients={'Мясо': 5, 'Соль': 6, 'Панировка': 8},
                recipe='Lorem Ipsum',
                image='filepath',
                author='john',
            )

            session.add_all(
                [
                    category_first,
                    category_second,
                    recipe_borsch,
                    recipe_paste,
                    recipe_cutlets,
                ]
            )
            session.commit()

    @staticmethod
    def select_last_recipes(limit_notes: int = 10) -> list:
        with session_factory() as session:
            query = (
                select(RecipeDish)
                .order_by(RecipeDish.published.desc())
                .limit(limit_notes)
            )
            result = session.execute(query).scalars().all()
            return result
