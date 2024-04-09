import allure
import requests
from data import BaseData


courier = '/api/v1/courier'
courier_login = '/api/v1/courier/login'
courier_delete = '/api/v1/courier/'

class CreateNewCourier:
    @allure.step('Создание нового курьера')
    def create_new_courier(self, **kwargs):
        payload = {}
        params = ["login", "password", "first_name"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.post(BaseData.BASE_URL + courier, data=payload, timeout=10)


class LoginCourier:
    @allure.step('Авторизация курьера')
    def login_courier(self, **kwargs):
        payload = {}
        params = ["login", "password"]

        for param in params:
            if param in kwargs:
                payload[param] = kwargs[param]

        return requests.post(BaseData.BASE_URL + courier_login, data=payload, timeout=10)


class DeleteCourier:

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id=None):
        return requests.delete(BaseData.BASE_URL + courier_delete + courier_id, timeout=10)
