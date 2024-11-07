import requests

from rest_framework import status
from config.settings import CUR_API_URL, CUR_API_KEY


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        url=f'{CUR_API_URL}v3/latest?apikey={CUR_API_KEY}&currencies=RUB')
    if response.status_code == status.HTTP_200_OK:
        rub_course = response.json()['data']['RUB']['value']
        usd_price = rub_price * rub_course
    return usd_price
