# weather_app/views.py

from django.shortcuts import render
from django.conf import settings
from .weather_utils import get_weather_data  # Your function from weather_utils.py
import os

def weather_view(request):
    """
    Display weather data for a specified city.
    """
    weather_data = None
    city = None
    error = None

    api_key = os.getenv("OPENWEATHER_API_KEY")  # Ensure .env is loaded

    if not api_key:
        error = "API key not set. Please check your environment variables."

    if request.method == "POST":
        city = request.POST.get("city")
        if city and api_key:
            weather_data = get_weather_data(api_key, city)
            if weather_data is None:
                error = "Could not fetch weather data. Try again later."
        elif not city:
            error = "Please enter a city or town name."

    context = {
        "weather_data": weather_data,
        "city": city,
        "error": error,
    }
    return render(request, "weather.html", context)