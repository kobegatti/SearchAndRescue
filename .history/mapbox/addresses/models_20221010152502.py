from django.db import models

# Create your models here.

class Address(models.Model):
   address = models.TextField()
   lat = models.FloatField(blank=True,null=True)
   lon = models.FloatField(blank=True,null=True)
