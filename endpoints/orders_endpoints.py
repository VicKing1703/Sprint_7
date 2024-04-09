import allure
import requests
from data import BaseData


orders = '/api/v1/orders'
orders_accept = '/api/v1/orders/'
orders_track = '/api/v1/orders/track'

class CreateNewOrder:
    @allure.step('Создание нового заказа')
    def create_new_order(self, **kwargs):
        payload = {}
        params = ["firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "comment",
                  "color"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.post(BaseData.BASE_URL + orders, data=payload, timeout=10)


class GetListOrders:
    @allure.step('Получение списка заказов')
    def get_list_orders(self, **kwargs):
        payload = {}
        params = ["courierId", "nearestStation", "limit", "page"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.get(BaseData.BASE_URL + orders, params=payload, timeout=30)


class AcceptOrder:
    @allure.step('Принятие заказа')
    def accept_order(self, order_id, **kwargs):
        payload = {}
        params = ["courierId"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.put(BaseData.BASE_URL + orders_accept + {order_id}, params=payload, timeout=30)


class GetOrderByNumber:
    @allure.step('Получение заказа по номеру')
    def get_order_by_number(self, **kwargs):
        payload = {}
        params = ["t"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.get(BaseData.BASE_URL + orders_track, params=payload, timeout=10)
