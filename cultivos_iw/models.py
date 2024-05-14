from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError



class Cultivo(models.Model):
    TROPICAL = 'Tropical'
    DRY = 'Seco'
    MILD = 'Templado'
    CONTINENTAL = 'Continental'
    COOL = 'Fríos'
    ANYONE = 'Cualquiera'
    
    BEGINNER = 'Principiante'
    MEDIUM = 'Medio'
    HARD = 'Difícil'
    
    SPRING = 'Primavera'
    SUMMER = 'Verano'
    AUTUMN = 'Otoño'
    WINTER = 'Invierno'
    

    SUN ='Sol'
    HALF_SHADOW = 'Media Sombra'
    SHADOW = 'Sombra'

    VEGETABLES = 'Hortalizas'
    FLOWERS = 'Flores'    
    AROMATICS = 'Aromáticas'

    WEATHER_CHOICES = [
        (TROPICAL, 'Tropical'),
        (DRY, 'Seco'),
        (MILD, 'Templado'),
        (CONTINENTAL, 'Continental'),
        (COOL, 'Fríos'),
        (ANYONE, 'Cualquiera'),
    ]
    
    DIFFICULTY_CHOICES = [
        (BEGINNER, 'Principiante'),
        (MEDIUM, 'Medio'),
        (HARD, 'Difícil'),
    ]
    
    SEASON_CHOICES = [
        (SPRING, 'Primavera'),
        (SUMMER, 'Verano'),
        (AUTUMN, 'Otoño'),
        (WINTER, 'Invierno'),
        (ANYONE, 'Cualquiera'),
    ]
    
    ILLUMINATION_CHOICES = [
        (SUN, 'Sol'), 
        (HALF_SHADOW, 'Media Sombra'),
        (SHADOW, 'Sombra')   
    ]
    
    TYPE_CHOICES = [
    (VEGETABLES, 'Hortalizas'),
    (FLOWERS, 'Flores'),
    (AROMATICS, 'Aromáticas')    
    ]
    
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    weather = models.CharField(max_length=12, choices=WEATHER_CHOICES, default=ANYONE)
    image = models.ImageField(upload_to='cultivos/')
    quantity = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default=BEGINNER)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES, default=SPRING)
    illumination = models.CharField(max_length=12, choices=ILLUMINATION_CHOICES, default=SUN)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=VEGETABLES)
    
    def __str__(self):
        return self.title