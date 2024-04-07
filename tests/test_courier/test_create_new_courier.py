import allure
from endpoints.courier_endpoints import CreateNewCourier
from data import DataCourier, DataResponseText


class TestCreateNewCourier:

    @allure.title('Тест создания нового курьера')
    @allure.description('Тест создания нового курьера с заполнением всех обязательных полей')
    def test_create_new_courier(self):
        response = CreateNewCourier().create_new_courier(login=DataCourier.LOGIN,
                                                         password=DataCourier.PASSWORD,
                                                         first_name=DataCourier.FIRST_NAME)
        assert response.status_code == 201 and response.json() == DataResponseText.OK_TRUE, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'

    @allure.title('Тест не возможности создания 2-х одинаковых курьеров')
    @allure.description('Тест не возможности создания 2-х курьеров с одинаковым логином')
    def test_create_two_couriers_with_the_same_login(self):
        login = DataCourier.LOGIN
        CreateNewCourier().create_new_courier(login=login,
                                              password=DataCourier.PASSWORD,
                                              first_name=DataCourier.FIRST_NAME)
        response = CreateNewCourier().create_new_courier(login=login,
                                                         password=DataCourier.PASSWORD,
                                                         first_name=DataCourier.FIRST_NAME)
        # текст ответа по факту немного дополнен, и логически дополнен верно.
        # По этому позволил себе дополнить и ожидаемый текст ответа
        assert response.status_code == 409 and response.json() == DataResponseText.LOGIN_EXIST, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'

    @allure.title('Тест не возможности создания курьера без логина')
    @allure.description('Тест не возможности создания курьера без передачи логина в теле запроса')
    def test_create_courier_without_login(self):
        response = CreateNewCourier().create_new_courier(password=DataCourier.PASSWORD,
                                                         first_name=DataCourier.FIRST_NAME)
        assert response.status_code == 400 and response.json() == DataResponseText.NOT_ENOUGH_DATA_FOR_CREATE, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'

    @allure.title('Тест не возможности создания курьера без пароля')
    @allure.description('Тест не возможности создания курьера без передачи пароля в теле запроса')
    def test_create_courier_without_password(self):
        response = CreateNewCourier().create_new_courier(login=DataCourier.LOGIN,
                                                         first_name=DataCourier.FIRST_NAME)
        assert response.status_code == 400 and response.json() == DataResponseText.NOT_ENOUGH_DATA_FOR_CREATE, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'
