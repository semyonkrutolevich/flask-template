import requests
import json
import sys
import os

CAPUSTA_TOKEN = os.getenv('CAPUSTA_TOKEN')
MAIN_PAYLOAD_LINK = os.getenv('MAIN_PAYLOAD_LINK')


capusta_token = CAPUSTA_TOKEN
main_payload_link = MAIN_PAYLOAD_LINK
pay_url = "https://api.capusta.space/v1/partner/payment"

def get_payload_data(feedbackuser_name, description, amount):
    payload_link = main_payload_link + feedbackuser_name
    payload = json.dumps({
        "id":payload_link,
        "amount":{
            "amount":amount,
            "currency":"RUB"
            },
        "projectCode":"putnik.live",
        "description":description, 
        "test": True
    })
    print(payload)
    headers = {
    'Authorization': capusta_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", pay_url, data = payload, headers=headers)
    print(response.text.encode('utf8'))
    return response


def payments_check(message):
    url = "https://api.capusta.space/v1/partner/status?transaction-id=" + main_payload_link + str(feedbackuser_name)

    payload = {}
    headers = {
    'Authorization': capusta_token
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    json_response = response.json()
    print(json_response['status'])
    if json_response['status'] == "SUCCESS":
        return 'Оплата прошла успешно'

get_payload_data("sema", "Ретрит выходного дня", 1000000)