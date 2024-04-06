import allure
import requests
from data import BaseData


class CreateNewCourier:
    @allure.step('Создание нового курьера')
    def create_new_courier(self, login="", password="", first_name=""):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(BaseData.BASE_URL + '/api/v1/courier', data=payload, timeout=10)


class LoginCourier:
    @allure.step('Авторизация курьера')
    def login_courier(self, login="", password=""):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(BaseData.BASE_URL + '/api/v1/courier/login', data=payload, timeout=10)


class DeleteCourier:

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id=None):
        return requests.delete(BaseData.BASE_URL + '/api/v1/courier/' + courier_id, timeout=10)
