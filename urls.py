from django.urls import include, path

urlpatterns = [
    path('', include('weather_app.urls')),
]