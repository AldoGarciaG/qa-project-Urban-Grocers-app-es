import requests
import data
import configuration

def post_create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body,
                         headers = data.headers)

def post_create_new_kit (kit_data , auth_token):
    actual_headers = data.headers.copy()
    actual_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kit_data,
                         headers = actual_headers)
