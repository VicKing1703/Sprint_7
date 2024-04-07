import allure
from endpoints.orders_endpoints import GetListOrders


class TestGetListOrders:

    @allure.title('Получение списка заказов')
    def test_get_list_orders(self):
        response = GetListOrders().get_list_orders()
        assert response.status_code == 200 and type(response.json()["orders"]) == list, \
            f'Код ответа {response.status_code} и тип данных {type(response.json()["orders"])}'
