import allure
import requests
from data import BaseData


class CreateNewOrder:
    @allure.step('Создание нового заказа')
    def create_new_order(self, first_name, last_name,
                         address, metro_station, phone,
                         rent_time, delivery_date, comment="", color=""):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }
        return requests.post(BaseData.BASE_URL + '/api/v1/orders', data=payload, timeout=10)


class GetListOrders:
    @allure.step('Получение списка заказов')
    def get_list_orders(self, courier_id=None, nearest_station=None, limit=None, page=None):
        payloads = {"courierId": courier_id, "nearestStation": nearest_station, "limit": limit, "page": page}
        return requests.get(BaseData.BASE_URL + '/api/v1/orders', params=payloads, timeout=30)


class AcceptOrder:
    @allure.step('Принятие заказа')
    def accept_order(self, order_id=None, courier_id=None):
        return requests.put(BaseData.BASE_URL + '/api/v1/orders/' + order_id, params=courier_id, timeout=10)


class GetOrderByNumber:
    @allure.step('Получение заказа по номеру')
    def get_order_by_number(self, order_id=None):
        payload = {"t": order_id}
        return requests.get(BaseData.BASE_URL + '/api/v1/orders/track', params=payload, timeout=10)