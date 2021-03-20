import requests
import json
#
client_id = '7771d2a4efd37585ee25'
client_secret = 'd49de7d8146a8d02649cd2169d97d26d'
#
# инициируем запрос на получение токена
#
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
#
# разбираем ответ сервера
j = json.loads(r.text)
print("j:", j)

# достаем токен
token = j["token"]
print("token:", token)
quit()
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)
print("j:", j)

