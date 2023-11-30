### Структура приложения

![Alt text](<docs/API structure.jpg>)
### Структура базы данных

![Alt text](<docs/DB structure.jpg>)

### Структура API

##### Recipe backend

```python

get('api/last_add_dish', description='Получение 10 последних рецептов блюд')
async def get_last_recipes() -> dict:
    Response = {'id': {'name': name,
                       'slug': slug,
	                   'category': category,
                       'description': description,
                       'published': published,
                       'image': image,
                       'author': author}
                }

    HTTP status code: 200
                      404
                      500


get('api/dish/{slug_dish}', description='Получение рецепта блюда по слагу')
async def get_one_recipe_dish():
    return {'message': 'Api recipe dish'}


get('api/dish', description='Получение списка рецептов по фильтрации')
async def get_filter_recipe_dish():
    return {'message': 'Api recipe dish'}


post('api/dish', description='Создание рецепта блюда')
async def create_recipe_dish():
    return {'message': 'Api recipe dish'}


patch('api/dish/{slug_dish}', description='Редактирование рецепта блюда')
async def edit_recipe_dish():
    return {'message': 'Api recipe dish'}


delete('api/dish/{slug_dish}', description='Удаление рецепта блюда')
async def delete_recipe_dish():
    return {'message': 'Api recipe dish'}


get('api/category/{slug_category}', description='Получение категории блюда по слагу')
async def get_one_category_dish():
    return {'message': 'Api recipe dish'}


get('api/category', description='Получение списка категорий по фильтрации')
async def get_filter_category_dish():
    return {'message': 'Api recipe dish'}


post('api/category', description='Создание категории блюд')
async def create_category_dish():
    return {'message': 'Api recipe dish'}


patch('api/category/{slug_category}', description='Редактирование категории блюд')
async def edit_category_dish():
    return {'message': 'Api recipe dish'}


delete('api/category/{slug_category}', description='Удаление категории блюд')
async def delete_category_dish():
    return {'message': 'Api recipe dish'}
```

##### Authentication API

```python
'''ручка регестрации пользователя'''
post('/signup')

    Response: {
            id,
            nickname
    }

    Errors: 201
            400
            500
            
'''ручка аутенфикации пользователя'''
post('/login')

    Response: {
            id,
            nickname,
            role,
            JWToken

    }

    Errors: 200
            401
            500
```