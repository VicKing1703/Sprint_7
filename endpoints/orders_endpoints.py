import allure
import requests
from data import BaseData
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


orders_base_url = f'{BaseData.BASE_URL}/api/v1/orders'


class CreateNewOrder:
    @allure.step('Создание нового заказа')
    def create_new_order(self, **kwargs):
        payload = {}
        params = ["firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "comment",
                  "color"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.post(orders_base_url, data=payload, timeout=10)


class GetListOrders:
    @allure.step('Получение списка заказов')
    def get_list_orders(self, **kwargs):
        payload = {}
        params = ["courierId", "nearestStation", "limit", "page"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.get(orders_base_url, params=payload, timeout=30)


class AcceptOrder:
    @allure.step('Принятие заказа')
    def accept_order(self, order_id, **kwargs):
        payload = {}
        params = ["courierId"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.put(orders_base_url + "/" + order_id, params=payload, timeout=30)


class GetOrderByNumber:
    @allure.step('Получение заказа по номеру')
    def get_order_by_number(self, **kwargs):
        payload = {}
        params = ["t"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.get(orders_base_url + "/track", params=payload, timeout=10)
