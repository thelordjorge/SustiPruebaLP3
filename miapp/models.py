from django.db import models

# Create your models here.

class Region(models.Model):
    
    name = models.CharField(max_length=150,  verbose_name="Name")
    cases = models.CharField(max_length=150, verbose_name="Cases")
    deaths = models.CharField(max_length=150, verbose_name="Deaths")
    lethality = models.CharField(max_length=150, verbose_name="Lethality")
    image = models.ImageField(default='null', verbose_name="Miniatura", upload_to="regiones")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Creado")