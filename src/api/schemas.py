from pydantic import BaseModel, FilePath, Json


class CategoryDish(BaseModel):
    '''Модель категории блюд'''
    name_category: str
    slug_category: str


class RecipeDish(BaseModel):
    '''Модель рецептов блюд'''
    name_dish: str
    slug_dish: str
    description: str
    ingredients: Json
    recipe: str
    published: str
    auhtor: str
    category: CategoryDish.name_category
    image: FilePath
