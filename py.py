import requests
import json
url = 'https://www.cbr-xml-daily.ru/latest.js'
res = requests.get(url)
with open('data.json', 'w') as file:
     json.dump(res.json(), file, indent=2)

a = res.json()
kzt=a['rates']['KZT']
print(f'1 рубль в тенге:{kzt} KZT')
