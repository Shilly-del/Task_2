import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters)
                            for i in range(length))
    return random_string


def create_incorrect_field(payload, key):

    wrong = payload.copy()
    wrong[key] = f"{wrong[key]}{random.randint(100, 999)}"

    return wrong


def change_field(payload, key):

    wrong = payload.copy()
    wrong[key] = f"{wrong[key]}{random.randint(100, 999)}"

    return wrong


def create_ingredient_list(ingredients, n):
    ingredient_list = ingredients['data']
    result = []

    [result.append(ingredient['_id']) for ingredient in ingredient_list]
    random.shuffle(result)
    return result[:n]
