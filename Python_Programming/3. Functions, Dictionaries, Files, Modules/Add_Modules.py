import requests
r = requests.get("http://example.com")      # Простой GET запрос
print(r.text)                               # Вывод ответа от сервера

url = "http://example.com"
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params = par)         # Передача параметров в запрос
print(r.url)           # Сформированный url-адрес с учетом параметров GET запроса