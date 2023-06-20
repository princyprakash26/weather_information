# Getting weather information

import requests
from pprint import pprint
import yaml



with open('config.yaml') as f:
    config = yaml.safe_load(f)

API_kEY = config['API_kEY']
base_url = config['base_url']

city = input("enter the city:")

url = f"{base_url}?q={city}&appid={API_kEY}"


weather_date = requests.get(url).json()

pprint(weather_date)