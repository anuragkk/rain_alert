api_key = "c199d164a4c52e89df9a8609ff9b9422"
import requests

parameters = {
    "lat": 39.082520,
    "lon": -94.582306,
    "appid": api_key,
    "cnt": 4

}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

will_rain = False
for entry in weather_data["list"]:
    if "weather" in entry and entry["weather"]:
        condition_code = entry["weather"][0]["id"]
        if int(condition_code) < 600:
            will_rain = True
if will_rain:
    print("Bring an Umbrella")
# weather_ids = [entry["weather"][0]["id"] for entry in weather_data["list"]]
#
# for data in weather_ids:
#     if data < 600:
#         print(f"it might  rain, your code is {data}, so bring umbrella")
