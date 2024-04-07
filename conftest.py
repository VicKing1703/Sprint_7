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
    create = CreateNewCourier().create_new_courier(login=login, password=password, first_name=first_name)
    assert create.status_code == 201, f'Код ответа {create.status_code} и текст ответа {create.text}'

    # логинимся новым курьером и получем его id
    login_courier = LoginCourier().login_courier(login=login, password=password)
    assert login_courier.status_code == 200, (f'Код ответа {login_courier.status_code} '
                                              f'и текст ответа {login_courier.text}')
    courier_id = str(login_courier.json()['id'])

    yield courier_id

    # удаляем курьера после тестов
    delete = DeleteCourier().delete_courier(courier_id)
    assert delete.status_code == 200, f'Код ответа {delete.status_code} и текст ответа {delete.text}'


@pytest.fixture
def get_track_by_create_new_order():
    # Создаём заказ и получаем его трек
    response = CreateNewOrder().create_new_order(firstName=DataOrder.FIRST_NAME,
                                                 lastName=DataOrder.LAST_NAME,
                                                 address=DataOrder.ADDRESS,
                                                 metroStation=DataOrder.METRO_STATION,
                                                 phone=DataOrder.PHONE,
                                                 rentTime=DataOrder.RENT_TIME,
                                                 deliveryDate=DataOrder.DELIVERY_DATE,
                                                 color=list(DataOrder.SCOOTER_COLOUR[random.randint(0, 1)]))
    assert response.status_code == 201, f'Код ответа {response.status_code} и текст ответа {response.text}'

    track = str(response.json()['track'])

    yield track


@pytest.fixture
def get_order_id_by_track(get_track_by_create_new_order):
    track = get_track_by_create_new_order

    response = GetOrderByNumber().get_order_by_number(track=track)
    assert response.status_code == 200, f'Код ответа {response.status_code} и текст ответа {response.text}'

    order_id = str(response.json()['orders'][0]['id'])

    yield order_id
