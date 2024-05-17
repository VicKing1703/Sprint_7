import allure
from data import DataResponseText, DataCourier
from endpoints.courier_endpoints import DeleteCourier, CreateNewCourier, LoginCourier


class TestDeleteCourier:

    @allure.title('Тест удаления существующего курьера')
    @allure.description('Тест удаления курьера')
    def test_delete_courier(self):
        login = DataCourier.LOGIN
        password = DataCourier.PASSWORD

        CreateNewCourier().create_new_courier(login=login,
                                              password=password,
                                              first_name=DataCourier.FIRST_NAME)
        courier_id = str(LoginCourier().login_courier(login=login, password=password).json()['id'])

        response = DeleteCourier().delete_courier(courier_id)
        assert response.status_code == 200 and response.json() == DataResponseText.OK_TRUE, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'


    @allure.title('Тест удаления несуществующего курьера')
    @allure.description('Тест удаления несуществующего id курьера')
    def test_delete_nonexistent_courier(self):
        response = DeleteCourier().delete_courier(courier_id='999999')
        assert response.status_code == 404 and response.json() == DataResponseText.NONEXISTENT_COURIER, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'


    @allure.title('Тест удаления курьера без передачи id')
    @allure.description('Тест удаления курьера без передачи id в теле запроса')
    def test_delete_courier_without_id(self):
        response = DeleteCourier().delete_courier("")
        assert response.status_code == 400 and response.json() == DataResponseText.NOT_ENOUGH_DATA_FOR_DELETE, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'
