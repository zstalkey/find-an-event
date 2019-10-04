from django.forms import ModelForm, SplitDateTimeField, ValidationError
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Event, Category, Account

class CreateEventForm(ModelForm):
    
    class Meta:
        model = Event
        exclude = ['host']
        # widgets = {'start_time': widgets.AdminSplitDateTime, 'end_time': widgets.AdminSplitDateTime,}

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]