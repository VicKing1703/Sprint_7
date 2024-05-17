import random
import pytest
from data import DataCourier, DataOrder
from endpoints.courier_endpoints import CreateNewCourier, LoginCourier, DeleteCourier
from endpoints.orders_endpoints import CreateNewOrder, GetOrderByNumber


@pytest.fixture
def create_login_and_delete_new_courier():
    # задаём необходимые параметры нгового курьера
    login = DataCourier.LOGIN
    password = DataCourier.PASSWORD
    first_name = DataCourier.FIRST_NAME

    # создаем нового курьера
    CreateNewCourier().create_new_courier(login=login, password=password, first_name=first_name)

    # логинимся новым курьером и получем его id
    login_courier = LoginCourier().login_courier(login=login, password=password)

    courier_id = str(login_courier.json()['id'])

    yield courier_id

    # удаляем курьера после тестов
    DeleteCourier().delete_courier(courier_id)


@pytest.fixture
def get_track_by_create_new_order():
    # Создаём заказ и получаем его трек
    response = CreateNewOrder().create_new_order(firstName=DataOrder.FIRST_NAME,
                                                 lastName=DataOrder.LAST_NAME,
                                                 address=DataOrder.ADDRESS,
                                                 metroStation=DataOrder.METRO_STATION,
                                                 phone=DataOrder.PHONE,
                                                 rentTime=DataOrder.RENT_TIME,
                                                 deliveryDate=DataOrder.DELIVERY_DATE)

    track = str(response.json()['track'])
    return track


@pytest.fixture
def get_order_id_by_track(get_track_by_create_new_order):
    track_number = get_track_by_create_new_order

    response = GetOrderByNumber().get_order_by_number(t=track_number)

    print(response.json())  # Добавьте эту строку для вывода данных JSON
    order_id = str(response.json()['order']['id'])
    print(order_id)

    return order_id
