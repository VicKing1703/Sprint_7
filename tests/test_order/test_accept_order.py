import allure
from conftest import create_login_and_delete_new_courier, get_order_id_by_track, get_track_by_create_new_order
from data import DataResponseText
from endpoints.orders_endpoints import AcceptOrder

# Не смог победить эьо доп задание. Из-за него не попал в ухдящий мягкий дедлайн...
class TestAcceptOrder:

    @allure.title('Принятие заказа с id курьера и id заказа')
    @allure.description('Принятие заказа с передачей id курьера и id заказа в запросe')
    def test_accept_order(self, create_login_and_delete_new_courier, get_order_id_by_track, get_track_by_create_new_order):

        courier_id = create_login_and_delete_new_courier
        order_id = get_order_id_by_track

        print(order_id, courier_id)
        response = AcceptOrder().accept_order(order_id, courierId=courier_id)

        assert response.status_code == 200 and response.json() == DataResponseText.OK_TRUE, \
            f'Код ответа {response.status_code} и текст ответа {response.text}'
