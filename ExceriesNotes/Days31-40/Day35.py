# day 35 api keys, authentication, environment variables, sending SMS
import requests

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "487ec581e0b8af779fc6f840b03e9204"
weather_params = {
    "lat": 42.360081,
    "lon": -71.058884,
    "appid": api_key,
}

response = requests.get(OWM_endpoint, params=weather_params)
# print(response.status_code)
print(response.json())