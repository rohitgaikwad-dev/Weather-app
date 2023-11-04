import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    WEATHERBIT_API_KEY = open("API_KEY", "r").read()
    current_weather_url = "https://api.weatherbit.io/v2.0/current"
    forecast_url = "https://api.weatherbit.io/v2.0/forecast/daily"

    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(
            city1, WEATHERBIT_API_KEY, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(
                city2, WEATHERBIT_API_KEY, current_weather_url, forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
            "weather_data2": weather_data2,
            "daily_forecasts2": daily_forecasts2
        }

        return render(request, "weather_app/index.html", context)
    else:
        return render(request, 'weather_app/index.html')

def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    current_weather_params = {
        "city": city,
        "key": api_key
    }
    
    forecast_params = {
        "city": city,
        "key": api_key,
        "days": 5  # Number of days for the forecast (5-day forecast)
    }

    response = requests.get(current_weather_url, params=current_weather_params).json()
    
    if 'error' in response:
        return None, None  # Handle error response from Weatherbit here

    forecast_response = requests.get(forecast_url, params=forecast_params).json()

    weather_data = {
        "city": city,
        "temperature": response['data'][0]['temp'],
        "description": response['data'][0]['weather']['description'],
        "icon": response['data'][0]['weather']['icon']
    }

    daily_forecasts = []
    for daily_data in forecast_response['data']:
        daily_forecasts.append({
            "day": daily_data['datetime'],
            "min_temp": daily_data['min_temp'],
            "max_temp": daily_data['max_temp'],
            "description": daily_data['weather']['description'],
            "icon": daily_data['weather']['icon']
        })

    return weather_data, daily_forecasts
