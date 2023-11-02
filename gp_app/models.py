from django.db import models
from django.urls import reverse
from django import forms

CITIES = (
    ('Colorado Springs', 'Colorado Springs'),
    ('Denver', 'Denver'),
    ('Fort Collins', 'Fort Collins'))
'''
class City(models.Model):
    CITIES = (
    ('Colorado Springs', 'Colorado Springs'),
    ('Denver', 'Denver'),
    ('Fort Collins', 'Fort Collins'))
    name = models.CharField(choices=CITIES, max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("index-city", args=[str(self.__str__)])
    
'''


class Business(models.Model):
    ACTIVE = ((True,'True'), (False,'False'))
    name = models.CharField("Name", max_length=200)
    email = models.CharField("Email", max_length=200)
    #city = models.ForeignKey(City, on_delete=models.CASCADE, default=None)
    city = models.CharField("Location", choices=CITIES, max_length=200)
    address = models.CharField("Address", max_length=200)
    phone_number = models.CharField("Phone", max_length=10)
    is_open = models.BooleanField("Open", default=True, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('business-detail', args=[str(self.id)])

