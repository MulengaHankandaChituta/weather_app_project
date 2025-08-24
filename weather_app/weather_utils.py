import requests

def get_weather_data(api_key, city):
    """
    Fetches weather data for a given city using OpenWeatherMap API.
    
    Parameters:
        api_key (str): Your OpenWeatherMap API key.
        city (str): The name of the city to fetch weather data for.

    Returns:
        dict: A dictionary containing weather data for the specified city, or None if an error occurs.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"  # Use HTTPS
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raise error for HTTP errors
        return response.json()
        print("Weather API response:", data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather for {city}: {e}")  # Log errors
        return None
