import requests
API_URL = "http://api.openweathermap.org/data/2.5/weather"
City = input("City? ")

parameters = {
    "q" : City,
    "appid" : "ca4b7ba3909c78d58c771e623ad91913",
    "units" : "metric"
}

res = requests.get(API_URL, params = parameters)
# print(res.status_code)
# print(res.headers["Content-Type"])
print(res.json())
data = res.json()
template = "Current temperature in {} is {}"
# print(data["main"]["temp"])
print(template.format(City, data["main"]["temp"]))