from django.db import models
from django.forms import ModelForm

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    events = models.ManyToManyField("Event")

    def __str__(self):
        return self.name

class CreateEventForm(ModelForm):
    title = Event.title
    location = Event.location
    venue = Event.venue
    start_time = Event.start_time
    end_time = Event.end_time