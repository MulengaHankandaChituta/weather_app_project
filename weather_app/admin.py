from django.contrib import admin
from .models import City, WeatherData, UserSearch, FavoriteCity

# Basic registration of models in the admin interface
admin.site.register(City)
admin.site.register(WeatherData)
admin.site.register(UserSearch)
admin.site.register(FavoriteCity)

