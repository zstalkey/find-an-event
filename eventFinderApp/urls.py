from django.urls import path
from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('my-account/', views.account, name='account'),
    # event-finder/event_creator_form
    path('event_creator_form/', views.add_event, name='event_creator_form'),
    #event-finder/edit_event/<int:pk>
    path('edit_event/<int:pk>', views.EditEventView.as_view(), name= 'edit_event'),
    path('addeventview/', views.AddEventView.as_view(), name='addeventview'),
]