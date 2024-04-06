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


# courier = DataCourier
# print(courier.FIRST_NAME, courier.PASSWORD, courier.LOGIN, sep='\n')
# print()
# order = DataOrder
# print(type(order.FIRST_NAME), order.FIRST_NAME,
#       type(order.LAST_NAME), order.LAST_NAME,
#       type(order.ADDRESS), order.ADDRESS,
#       type(order.PHONE), order.PHONE,
#       type(order.DELIVERY_DATE), order.DELIVERY_DATE,
#       type(order.SCOOTER_COLOUR), order.SCOOTER_COLOUR,
#       type(order.RENT_TIME), order.RENT_TIME,
#       type(order.METRO_STATION), order.METRO_STATION, sep='\n')
