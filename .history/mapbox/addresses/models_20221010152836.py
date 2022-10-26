import geocoder

from django.db import models

# Create your models here.

class Address(models.Model):
   address = models.TextField()
   lat = models.FloatField(blank=True,null=True)
   long = models.FloatField(blank=True,null=True)

   def save(self, *args, **kwargs):
      g = geocoder.mapbox(self.address, key="TOKEN")
      g = g.latlng # [lat, lng]
      self.lat = g[0]
      self.long = g[1]
      return super(Address, self).save(*args, **kwargs)

