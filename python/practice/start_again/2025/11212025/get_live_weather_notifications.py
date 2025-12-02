#   https://www.geeksforgeeks.org/python/get-live-weather-desktop-notifications-using-python/

import requests
from plyer import notification
city = "San Francisco"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
get_parm = {"name": city , "count": 1}
geo_res = requests.get(geo_url, params=get_parm).json()

if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "lattitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_res = requests.get(weather_url, params=weather_params).json()
    if "current_weather" in weather_res:
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]
        weather_info = f"{City}: {temp}°C, Wind: {wind} km/h"
        print ("Weather Info:", weather_info)
        notification.notify(
            title=f"Weather in {city}",
            message = weather_info,
            timeout=5
        )
    else:
        print ("Weather information not found.")
else:
    print ("City not found.")