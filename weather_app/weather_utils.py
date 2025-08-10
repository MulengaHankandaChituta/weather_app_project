import requests

def get_weather_data(api_key, city):
    """
    Fetches weather data for a given city using OpenWeatherMap API.
    
    Parameters:
    api_key(str):Your OpenWeatherMap API key.
    ciity(str):The name of the city to fetch the weather data for.

    returns:  
    dict: A dictionary containing weather data for  the specified city.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raises an error for bad responses
        return response.json()
    except requests.exceptions.RequestException:
        return None