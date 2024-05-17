import allure

from data import DataResponseText
from endpoints.orders_endpoints import GetOrderByNumber
from conftest import get_track_by_create_new_order


class TestGetOrderByNumber:

    @allure.title('Получение заказа по номеру трека')
    @allure.description('Получение заказа по номеру трека в запросе')
    def test_get_order_by_number(self, get_track_by_create_new_order):

        track = get_track_by_create_new_order

        response = GetOrderByNumber().get_order_by_number(t=track)
        assert response.status_code == 200 and "order" in response.json(), \
            f'Код ответа {response.status_code} и текст ответа {response.text}'


    @allure.title('Получение ошибки по не существующему номеру трека')
    @allure.description('Получение ошибки по существующему номеру трека в запросе')
    def test_get_order_by_nonexistent_number(self):

        response = GetOrderByNumber().get_order_by_number(t="999999999")
        assert response.status_code == 404 and response.json() == DataResponseText.NOT_FOUND_ORDER

    @allure.title('Получение ошибки без передачи номера заказа')
    @allure.description('Получение ошибки без передачи номера заказа в запросе')
    def test_get_order_by_no_number(self):

        response = GetOrderByNumber().get_order_by_number()
        assert response.status_code == 400 and response.json() == DataResponseText.NO_DATA_FOR_SEARCH
