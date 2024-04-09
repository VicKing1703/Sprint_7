import random
from mimesis import Person, Locale, Address, Datetime


class BaseData:

    BASE_URL = 'http://qa-scooter.praktikum-services.ru'


class DataCourier:

    FIRST_NAME = Person().name()
    PASSWORD = Person().password(length=5)
    LOGIN = Person().username()


class DataOrder:

    FIRST_NAME = Person(locale=Locale.RU).name()
    LAST_NAME = Person(locale=Locale.RU).surname()
    ADDRESS = Address(locale=Locale.RU).address()
    PHONE = Person(locale=Locale.RU).telephone(mask='+79##########')
    DELIVERY_DATE = Datetime().date(2024, 2025)
    SCOOTER_COLOUR = ['GREY', 'BLACK']
    RENT_TIME = random.randint(1, 7)
    METRO_STATION = random.randint(1, 224)


class DataResponseText:
    OK_TRUE = {'ok': True}
    LOGIN_EXIST = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    NOT_ENOUGH_DATA_FOR_CREATE = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    ACCOUNT_NOT_FOUND = {"code": 404, "message": "Учетная запись не найдена"}
    INSUFFICIENT_LOGIN_DATA = {"code": 400, "message": "Недостаточно данных для входа"}
    NONEXISTENT_COURIER = {"code": 404, "message": "Курьера с таким id нет."}
    NOT_ENOUGH_DATA_FOR_DELETE = {"message": "Недостаточно данных для удаления курьера"}
    NOT_FOUND_ORDER = {"code": 404, "message": "Заказ не найден"}
    NO_DATA_FOR_SEARCH = {"code": 400, "message": "Недостаточно данных для поиска"}
