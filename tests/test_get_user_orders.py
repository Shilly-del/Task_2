import requests
import pytest
import allure

from constants import *
from helpers.data_gen import *
from apios.order import Order


class TestGetUserOrders:
    @allure.title('Проверка получения списка заказов авторизованным пользователем')
    def test_get_user_orders_successful(self, user):
        """
        Регистрируем пользователя, запрашиваем список его заказов.
        """
        get = requests.get(
            Url.ORDERS, headers=user.headers)

        assert get.status_code == 200
        assert get.json()['success'] == True

    @allure.title('Проверка получения списка заказов пользователя без авторизации')
    def test_get_user_orders_unautorized(self, user):
        """
        Регистрируем пользователя, запрашиваем список его заказов.
        """
        get = requests.get(Url.ORDERS)

        assert get.status_code == 401
        assert get.json()['message'] == "You should be authorised"
