# Weather App – Django Integration

**Author:** Mulenga Hankanda Chituta  
**License:** MIT License (2025)  

This project is a **Django web application** that integrates the functionality of my standalone Python + Tkinter Weather App into a browser-based interface.  
It fetches real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/api) and displays it to the user in a clean, responsive web page.


## Features (Planned for Django Version)

- Fetch **live weather data** by entering a city name.
- Display:
  - City name
  - Temperature (°C)
  - Humidity (%)
  - Weather description
- Responsive, mobile-friendly design.
- Use Django forms for user input.
- Secure API key storage using `.env` and `python-dotenv`.
- Handle network errors and invalid input gracefully.



## Requirements

- Python 3.8+
- Django 5.x (or your installed version)
- Dependencies:
  - `requests`
  - `python-dotenv`
- OpenWeatherMap API key (Free tier available)



## Installation & Setup

1. **Clone the Repository**  

   git clone https://github.com/yourusername/django-weather-app.git
   cd django-weather-app

Create & Activate a Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install Dependencies
pip install django requests python-dotenv
Create the .env File

In the project root, add:
OPENWEATHER_API_KEY=your_api_key_here

Run Database Migrations
python manage.py migrate

Start the Development Server
python manage.py runserver
Usage (Planned Workflow)

Go to the homepage.
Enter the city name in the search form.

View the current weather data fetched via OpenWeatherMap API.

File Structure (Planned)
django-weather-app/
│
├── weatherapp/                # Django app for weather functionality
│   ├── templates/weatherapp/   # HTML templates
│   ├── static/weatherapp/      # CSS, JS
│   ├── views.py                # Handles API requests & rendering
│   ├── forms.py                # Django form for city input
│   └── urls.py                 # App routes
│
├── django_weather/             # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── .env                        # API key storage (not committed)
├── manage.py
└── README.md

Future Enhancements
Save user search history in the database.

Add a forecast view for multi-day weather data.

Include geolocation-based search.

Provide a REST API endpoint for weather queries.

License
This project is licensed under the MIT License – see the LICENSE file for details.

