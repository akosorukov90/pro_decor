import os
from pprint import pprint
from logger_1 import logger_1
from logger_2 import param_logger


@logger_1
def cook_book_create(file_path):
    cook_book = {}
    count_str = 0
    food = ''
    prop = ['ingredient_name', 'quantity', 'measure']
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line == '\n':
                count_str = 0
            else:
                if count_str == 0:
                    count_str += 1
                    food = line[:len(line) - 1]
                    cook_book[food] = []
                elif count_str == 1:
                    count_str += 1
                elif count_str == 2:
                    ingredient = line.split('|')
                    cook_book[food].append({prop[0]: ingredient[0].strip(), prop[1]: int(ingredient[1].strip()),
                                            prop[2]: ingredient[2].strip()[:len(ingredient[2]) - 1]})
        return cook_book


@param_logger(param='debug_2.log')
def get_shop_list_by_dishes(dishes, person_count, file_path):
    cook_book = cook_book_create(file_path)
    shop_list = {}
    for food in dishes:
        for key, value in cook_book.items():
            if key == food:
                for ingredient in value:
                    name = ingredient.get('ingredient_name')
                    measure = ingredient.get('measure')
                    quantity = ingredient.get('quantity')
                    if shop_list.get(name):
                        shop_list.get(name).update({'measure': measure, 'quantity': quantity * person_count + shop_list.get(name).get('quantity')})
                    else:
                        shop_list[name] = {'measure': measure, 'quantity': quantity * person_count}
    return shop_list


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    #pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
    get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
