from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'users'

urlpatterns = [
    path('event-finder/', include('eventFinderApp.urls')),
    path('register/', views.Register.as_view(), name='register'),
]