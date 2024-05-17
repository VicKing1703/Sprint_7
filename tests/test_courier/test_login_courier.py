import allure
from data import DataCourier, DataResponseText
from endpoints.courier_endpoints import LoginCourier, CreateNewCourier


# Проверки создавал по реальным ответам в Postman, иначе тесты, что должны возвращать 400-е, падают.
# В реальности в теле ответа на все 400-е ошибки содержится еще раз код ошибки,
# например {"code": 400, "message": "Недостаточно данных для входа"}, в документации содержится только "message"
# Для простоты изменения ответа вывел тексты ответов в файл data.py
class TestLoginCourier:

    @allure.title('Тест авторизации курьера')
    @allure.description('Тест авторизации курьера с корректными данными')
    def test_login_courier(self):
        password = DataCourier.PASSWORD
        login = DataCourier.LOGIN
        CreateNewCourier().create_new_courier(login=login, password=password, first_name=DataCourier.FIRST_NAME)
        response = LoginCourier().login_courier(login=login, password=password)
        assert response.status_code == 200 and 'id' in response.json(), \
            f'Код ответа {response.status_code} и текст ответа {response.text}'

    @allure.title('Тест авторизации курьера с некорректными паролем')
    @allure.description('Тест авторизации курьера с передаваемым в теле запроса пароля со значением логина')
    def test_login_courier_with_incorrect_password(self):
        login = DataCourier.LOGIN
        CreateNewCourier().create_new_courier(login=login,
                                              password=DataCourier.PASSWORD,
                                              first_name=DataCourier.FIRST_NAME)
        response = LoginCourier().login_courier(login=login, password=login)
        assert response.status_code == 404 and response.json() == DataResponseText.ACCOUNT_NOT_FOUND, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'

    @allure.title('Тест авторизации курьера без параметра логин')
    @allure.description('Тест авторизации курьера без передачи логина в теле запроса')
    def test_login_courier_without_login(self):
        password = DataCourier.PASSWORD
        CreateNewCourier().create_new_courier(login=DataCourier.LOGIN,
                                              password=password,
                                              first_name=DataCourier.FIRST_NAME)
        response = LoginCourier().login_courier(password=password)
        assert response.status_code == 400 and response.json() == DataResponseText.INSUFFICIENT_LOGIN_DATA, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'

    @allure.title('Тест авторизации курьера с пустым параметром пароль')
    @allure.description('Тест авторизации курьера с пустым параметром пароль в теле запроса')
    def test_login_courier_without_password(self):
        password = ""
        login = DataCourier.LOGIN
        CreateNewCourier().create_new_courier(login=login,
                                              password=DataCourier.PASSWORD,
                                              first_name=DataCourier.FIRST_NAME)
        response = LoginCourier().login_courier(login=DataCourier.LOGIN, password=password)
        assert response.status_code == 400 and response.json() == DataResponseText.INSUFFICIENT_LOGIN_DATA, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'
