from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from .forms import CreateEventForm
from django.urls import reverse_lazy
from .models import Event


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


def account(request):
    return render(request, 'eventFinderApp/account.html')

class EventCreatorView(generic.DetailView):
    form_class = CreateEventForm
    success_url = reverse_lazy('login')
    template = 'eventFinderApp/event_creator_form.html'
    
#     def get(self, request):
#         form = CreateEventForm
#         context = {'form': CreateEventForm}
#         template = 'eventFinderApp/event_creator_form.html'
#         return render(request, template, context)

def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateEventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            form.save()
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
        return render(request, 'eventFinderApp/event_creator_form.html', {'CreateEventForm': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateEventForm()
        return render(request, 'eventFinderApp/event_creator_form.html', {'CreateEventForm': form})
