
import requests

def get_weather_data(api_key, city):
    """
    Fetch weather data from OpenWeatherMap API for a given city.

    Parameters:
    - api_key (str): Your OpenWeatherMap API key.
    - city (str): Name of the city.

    Returns:
    - dict: Weather data JSON if successful.
    - None: If there was an error fetching data.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")  # Optional logging
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception: {req_err}")

    return None