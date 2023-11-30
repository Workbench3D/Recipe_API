from fastapi import APIRouter, HTTPException

from api.database import RecipeORM


router = APIRouter(prefix='/api', tags=['api'])


@router.get('/last_add_dish',
            description='Получение 10 последних рецептов блюд')
async def get_last_recipes() -> dict:
    result = RecipeORM.select_last_recipes()
    if not result:
        raise HTTPException(status_code=404)

    last_recipe = {i.id: {'name': i.name,
                          'slug': i.slug,
                          'category': i.category,
                          'description': i.description,
                          'published': i.published,
                          'image': i.image,
                          'author': i.author} for i in result}

    return last_recipe


@router.get('/dish/{slug_dish}',
            description='Получение рецепта блюда по слагу')
async def get_one_recipe_dish():
    return {'message': 'Api recipe dish'}


@router.get('/dish', description='Получение списка рецептов по фильтрации')
async def get_filter_recipe_dish():
    return {'message': 'Api recipe dish'}


@router.post('/dish', description='Создание рецепта блюда')
async def create_recipe_dish():
    return {'message': 'Api recipe dish'}


@router.patch('/dish/{slug_dish}', description='Редактирование рецепта блюда')
async def edit_recipe_dish():
    return {'message': 'Api recipe dish'}


@router.delete('/dish/{slug_dish}', description='Удаление рецепта блюда')
async def delete_recipe_dish():
    return {'message': 'Api recipe dish'}


@router.get('/category/{slug_category}',
            description='Получение категории блюда по слагу')
async def get_one_category_dish():
    return {'message': 'Api recipe dish'}


@router.get('/category',
            description='Получение списка категорий по фильтрации')
async def get_filter_category_dish():
    return {'message': 'Api recipe dish'}


@router.post('/category', description='Создание категории блюд')
async def create_category_dish():
    return {'message': 'Api recipe dish'}


@router.patch('/category/{slug_category}',
              description='Редактирование категории блюд')
async def edit_category_dish():
    return {'message': 'Api recipe dish'}


@router.delete('/category/{slug_category}',
               description='Удаление категории блюд')
async def delete_category_dish():
    return {'message': 'Api recipe dish'}
