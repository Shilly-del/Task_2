import requests
import allure
import string

from constants import Url
from helpers.data_gen import *


class Order:

    @allure.step('Создание данных заказа')
    def __init__(self):
        self.payload = {"ingredients": []}

    @allure.step('Регистрация заказа')
    def register_order(self):
        self.payload["ingredients"] = create_ingredient_list(
            self.ingredients, 2)
        r = requests.post(Url.ORDERS, data=self.payload)
