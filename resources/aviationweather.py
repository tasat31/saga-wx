from typing import Dict
import requests

# See -> https://aviationweather.gov/data/api/#/
BASE_URL = 'https://aviationweather.gov/'

def get_metar(params: Dict)->str:
    url = BASE_URL + 'api/data/metar'

    response = requests.get(url, params=params)

    if (response.status_code == 200):
        return response.text
    else:
        return ''

def get_taf(params: Dict)->str:
    url = BASE_URL + 'api/data/taf'

    response = requests.get(url, params=params)

    if (response.status_code == 200):
        return response.text
    else:
        return ''

def get_stationinfo(params: Dict)->str:
    url = BASE_URL + 'api/data/stationinfo'

    response = requests.get(url, params=params)

    if (response.status_code == 200):
        return response.text
    else:
        return ''

