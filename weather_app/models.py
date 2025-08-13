from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}, {self.country}"

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='weather_records')
    temperature = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.FloatField()
    description = models.CharField(max_length=200)
    wind_speed = models.FloatField(null=True, blank=True)
    visibility = models.FloatField(null=True, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-recorded_at']
        verbose_name_plural = "Weather Data"
    
    def __str__(self):
        return f"{self.city.name} - {self.temperature}°C ({self.recorded_at.strftime('%Y-%m-%d %H:%M')})"
    
    def is_recent(self, minutes=30):
        """Check if weather data is recent (within specified minutes)"""
        return (timezone.now() - self.recorded_at).total_seconds() < (minutes * 60)

class UserSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    searched_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-searched_at']
    
    def __str__(self):
        user_info = self.user.username if self.user else f"Anonymous ({self.ip_address})"
        return f"{user_info} searched {self.city.name} at {self.searched_at.strftime('%Y-%m-%d %H:%M')}"

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_cities')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'city']
        ordering = ['-added_at']
    
    def __str__(self):
        return f"{self.user.username}'s favorite: {self.city.name}"