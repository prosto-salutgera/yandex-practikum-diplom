# Георгий Герасимов, 22-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import data

url_service="https://1a4beb66-dfb4-45d0-96f3-8a81d1a0d6be.serverhub.praktikum-services.ru"
create_order_path="/api/v1/orders"
get_order_list="/api/v1/orders/track?t="

#Создание заказа
def create_order():
    return requests.post(url_service + create_order_path,
                         json=data.order,
                         headers=data.headers)
response=create_order()
order_track=response.json()["track"]
#Получение заказа по трекеру
def get_order_by_track():
    return requests.get(url_service + get_order_list + f"{order_track}",
                        headers=data.headers)
response=get_order_by_track()
print(response.json())
#Тест проверки получения заказа по трекеру
def test_get_order():
    order_test_track=get_order_by_track()
    assert order_test_track.status_code == 200
