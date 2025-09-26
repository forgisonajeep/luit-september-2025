import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=0e77e5c5011e40578ca164408252109&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, 'is', description, 'and', temp, 'degrees')