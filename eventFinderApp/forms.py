from django.forms import ModelForm
from .models import Event, Category

class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 
        'location', 
        'venue', 
        'start_time', 
        'end_time', 
        'categories']
