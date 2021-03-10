import requests
API_URL = "http://api.openweathermap.org/data/2.5/weather"
City = input("City? ")

Parameters = {
    "q" : City,
    "appid" : "ca4b7ba3909c78d58c771e623ad91913",
    "units" : "metric"
#    "lang" : "ru"
}

res = requests.get(API_URL, params = Parameters)
# print(res.status_code)
# print(res.headers["Content-Type"])
print(res.json())       # returns json.loads(res.text) :)
data = res.json()
template = "Current temperature in {} is {}"
# print(data["main"]["temp"])
print(template.format(City, data["main"]["temp"]))