import random
import allure
from endpoints.orders_endpoints import CreateNewOrder
from data import DataOrder


class TestCreateNewOrder:

    @allure.title('Создание нового заказа с выбором одного из цветов: серый или чёрный')
    @allure.description('Создание нового заказа с передачей одного из цветов: серый или чёрный, в теле запроса')
    def test_create_new_order_with_one_color(self):
        responce = CreateNewOrder().create_new_order(firstName=DataOrder.FIRST_NAME,
                                                     lastName=DataOrder.LAST_NAME,
                                                     address=DataOrder.ADDRESS,
                                                     metroStation=DataOrder.METRO_STATION,
                                                     phone=DataOrder.PHONE,
                                                     rentTime=DataOrder.RENT_TIME,
                                                     deliveryDate=DataOrder.DELIVERY_DATE,
                                                     color=list(DataOrder.SCOOTER_COLOUR[random.randint(0, 1)]))
        assert responce.status_code == 201 and "track" in responce.json(), \
            f'Код ответа {responce.status_code} и текст ответа {responce.text}'

    @allure.title('Создание нового заказа с выбором обоих цветов')
    @allure.description('Создание нового заказа с передачей обоих цветов в теле запроса')
    def test_create_new_order_with_two_color(self):
        responce = CreateNewOrder().create_new_order(firstName=DataOrder.FIRST_NAME,
                                                     lastName=DataOrder.LAST_NAME,
                                                     address=DataOrder.ADDRESS,
                                                     metroStation=DataOrder.METRO_STATION,
                                                     phone=DataOrder.PHONE,
                                                     rentTime=DataOrder.RENT_TIME,
                                                     deliveryDate=DataOrder.DELIVERY_DATE,
                                                     color=DataOrder.SCOOTER_COLOUR)
        assert responce.status_code == 201 and "track" in responce.json(), \
            f'Код ответа {responce.status_code} и текст ответа {responce.text}'

    @allure.title('Создание нового заказа без выбора цвета')
    @allure.description('Создание нового заказа без передачи цвета в теле запроса')
    def test_create_new_order_without_color(self):
        responce = CreateNewOrder().create_new_order(firstName=DataOrder.FIRST_NAME,
                                                     lastName=DataOrder.LAST_NAME,
                                                     address=DataOrder.ADDRESS,
                                                     metroStation=DataOrder.METRO_STATION,
                                                     phone=DataOrder.PHONE,
                                                     rentTime=DataOrder.RENT_TIME,
                                                     deliveryDate=DataOrder.DELIVERY_DATE)
        assert responce.status_code == 201 and "track" in responce.json(), \
            f'Код ответа {responce.status_code} и текст ответа {responce.text}'
