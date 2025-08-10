from django.shortcuts import render
from django.conf import settings
from .weather_utils import get_weather_data

def weather_view(request):
    """
    View to render the weather data for a specified city.
    
    parameters:
    request: The HTTP request object.
    
    Returns:
    HttpResponse: Rendered HTML page with weather data or an error message.
    """
    weather_data = None
    city = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            api_key = settings.OPENWEATHER_API_KEY
            weather_data = get_weather_data(api_key, city)
            if weather_data is None:
                error = "Could not fetch weather data. Try again later."
        else:
            error = "Please enter a city or town name."

    return render(request, "weather.html", {
        "weather_data": weather_data,
        "city": city,
        "error": error,
    })