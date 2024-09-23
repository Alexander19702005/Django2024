from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }



def dish_view(request, dish_name):
    recipe = DATA.get(dish_name)


    if recipe is None:
        return render(request, 'calculator/error.html', {'message': 'Такого блюда нет в меню.'})


    servings = int(request.GET.get('servings', 1))


    extendeed_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}


    context = {
        'recipe': extendeed_recipe,
        'dish_name': dish_name,
        'servings': servings,
    }

    return render(request, 'calculator/index.html', context)