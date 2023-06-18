# Getting weather information

import requests
from pprint import pprint

API_kEY = '4a66611882e913b1e0200ba837522cbc'

city = input("enter the city:")

base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+ API_kEY

print(base_url)
weather_date = requests.get(base_url).json()

pprint(weather_date)