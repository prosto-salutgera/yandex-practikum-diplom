import sender_stand_request

#Тест проверки получения заказа по трекеру
def test_get_order():
    response_create_order = sender_stand_request.create_order()
    track = response_create_order.json()["track"]
    order_test_track = sender_stand_request.get_order_by_track(track)
    assert order_test_track.status_code == 200

