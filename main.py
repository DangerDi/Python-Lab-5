import requests
import json

print('1)')
r = requests.get("https://vk.com")
print(r)

print('\n2)')
print("Saint Petersburg,RU")
city_id = 536203
appid = "e2993f1304f72524c5d6e01c3f6721e4"
try:
    re = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    print(re)
    data = re.json()
    print("Погода :", data['weather'][0]['description'])
    print("Температура :", data['main']['temp'], "°C")
    print("Влажность :", data['main']['humidity'], "%")
    print("Атмосферное давление :", data['main']['pressure'], "hPa")
except Exception as e:
    print("Exception (weather):", e)
    pass

print('\n3)')
try:
    res = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    print(res)
    print(json.loads(res.text)['Valute']['USD']['Value'])
except Exception as e:
    print("Exception :", e)
    pass

print('\nDop')
try:
    resp = requests.get("https://postprice.ru/engine/russia/api.php", params={'from': 105064, 'to': 620000, 'mass': 40, 'valuation': 500, 'vat': 1})
    print(resp)
    print(json.loads(resp.text)["simple_letter"])
except Exception as e:
    print("Exception :", e)
    pass