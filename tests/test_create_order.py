import requests
import pytest
import allure

from constants import *
from helpers.data_gen import *
from apios.order import Order


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа авторизованным пользователем')
    def test_create_order_succesfull(self, user):
        """
        Регистрируем пользователя, создаём заказ.
        """
        user.get_ingredients()
        order = Order()
        order.payload["ingredients"] = create_ingredient_list(
            user.ingredients, 2)

        create_order = requests.post(
            Url.ORDERS, data=order.payload, headers=user.headers)

        assert create_order.status_code == 200
        assert create_order.json()['success'] == True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, user):
        """
        Регистрируем пользователя, создаём заказ без ингредиентов.
        """
        user.get_ingredients()
        order = Order()

        create_order = requests.post(
            Url.ORDERS, data=order.payload, headers=user.headers)

        assert create_order.status_code == 400
        assert create_order.json()['success'] == False

    @allure.title('Проверка создания заказа c неверным хешем ингредиента')
    def test_incorrect_login(self, user):
        """
        Регистрируем пользователя, создаём заказ с неверным хешем ингредиента.
        """
        user.get_ingredients()
        order = Order()
        ingredients = create_ingredient_list(user.ingredients, 2)
        ingredients[0] = f'{ingredients[0]}qwe'
        order.payload["ingredients"] = ingredients

        create_order = requests.post(
            Url.ORDERS, data=order.payload, headers=user.headers)

        assert create_order.status_code == 500
