# Георгий Герасимов, 22-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import create_auto_test
import data
import configuration

#Создание заказа
def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order,
                         headers=data.headers)
response = create_order()
print(response.json())


#Получение заказа по трекеру
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_LIST + f"{track}",
                        headers=data.headers)
