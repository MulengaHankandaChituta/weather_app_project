from django.shortcuts import render
import os
from .weather_utils import get_weather_data

def weather_view(request):
    """
    Display weather data for a specified city.
    """
    weather_data = None
    city = None
    error = None

    # Get API key from environment variables
    api_key = os.getenv("OPENWEATHER_API_KEY")
    print("🔑 API KEY FROM ENV:", api_key)  # Debug line
    if not api_key:
        error = "API key not set. Please check your environment variables."

    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            if api_key:
                weather_data = get_weather_data(api_key, city)
                if not weather_data:
                    error = f"Could not fetch weather data for {city}. Try again later."
            else:
                error = "API key missing."
        else:
            error = "Please enter a city name."

    context = {
        "weather_data": weather_data,
        "city": city,
        "error": error,
    }
    return render(request, "weather.html", context)
