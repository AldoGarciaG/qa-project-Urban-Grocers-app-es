import data
import sender_stand_request

def get_new_token():
    response = sender_stand_request.post_create_new_user(data.user_data)
    return response.json()["authToken"]

def get_new_kit(kit_data):
    actual_name = data.kit_data.copy()
    actual_name["name"] = kit_data
    return actual_name

def positive_assert_201(kit_data):
    response = sender_stand_request.post_create_new_kit(kit_data,get_new_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_data["name"]

def negative_assert_400(kit_data):
    response = sender_stand_request.post_create_new_kit(kit_data,get_new_token())
    assert response.status_code == 400

def test1_create_a_kit_with_1_letter():
    actual_kit_data = get_new_kit("a")
    positive_assert_201(actual_kit_data)

def test2_create_a_kit_with_511_letters():
    actual_kit_data = get_new_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert_201(actual_kit_data)

def test3_create_a_kit_with_empty_string():
    actual_kit_data = get_new_kit("")
    negative_assert_400(actual_kit_data)

def test4_create_a_kit_with_512_letters():
    actual_kit_data = get_new_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_400(actual_kit_data)

def test5_create_a_kit_with_special_characters():
    actual_kit_data = get_new_kit("№%@")
    positive_assert_201(actual_kit_data)

def test6_create_a_kit_with_allowed_spaces():
    actual_kit_data = get_new_kit("A Aaa")
    positive_assert_201(actual_kit_data)

def test7_create_a_kit_with_numbers():
    actual_kit_data = get_new_kit("123")
    positive_assert_201(actual_kit_data)

def test8_create_a_kit_without_parameters():
    actual_kit_data = get_new_kit()
    negative_assert_400(actual_kit_data)

def test8_create_a_kit_with_diferent_parameters():
    actual_kit_data = get_new_kit(123)
    negative_assert_400(actual_kit_data)