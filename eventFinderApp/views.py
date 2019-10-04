from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, redirect
from .forms import CreateEventForm, AccountForm
from django.urls import reverse_lazy, reverse
from .models import Event, Category, Account
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserChangeForm
from users.models import CustomUser
from .filters import EventFilter


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

    def get_contect_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilter(self.request.GET, queryset=self.get_queryset())
        return context


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

@login_required(login_url='login')
def account(request):
    events_list = Event.objects.filter(host=request.user)
    if request.method == 'POST':
        print(request.POST)
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    context = {'events_list': events_list, 'form': user_form}
    template_name = 'eventFinderApp/account.html'
    return render(request, template_name, context)   


def account(request):
    return render(request, 'eventFinderApp/account.html')

class EventCreatorView(generic.DetailView):
    form_class = CreateEventForm
    success_url = reverse_lazy('login')
    template_name = 'eventFinderApp/event_creator_form.html'
    
@login_required(login_url ='login')
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
            new_event = form.save(commit=False)
            #add the host
            new_event.host = request.user
            form.save()
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
        return render(request, 'eventFinderApp/event_creator_form.html', {'CreateEventForm': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateEventForm()
        return render(request, 'eventFinderApp/event_creator_form.html', {'CreateEventForm': form})
def account(request):
    return render(request, 'eventFinderApp/account.html')

class AddEventView(generic.View):
    template_name = 'eventFinderApp/addevent.html'
    form_class = CreateEventForm
    success_url = reverse_lazy('eventFinderApp:index')
# we have to use reverse_lazy so that urls.py can load our class
# and not get stuck in a recursive loop 

    def form_context(self, eventform):
        # assign the form to the context
        return {'form': CreateEventForm}

    # in the class basded view we handle the GET request with a get() function
    def get(self, request):
        # create our form instance
        CreateEventForm = self.form_class()
        # return our template with our contex
        return render(request, self.template, self.form_context(eventform))

    # in the class based view we handle the POST request with a post() function
    def post(self, request):
        # we create our form instance with the data from the request
        CreateEventForm = self.form_class(request.POST)
        # check if the form is valid
        if CreateEventForm.is_valid():
            # save the data of the form
            CreateEventForm.save()
            # redirect to the list of events 
            return HttpResponseRedirect(self.success_url)
        # if the form isn't valid return the form (with automatic errors)
        # build the response with our template
        return render(request, self.template, self.form_context(CreateEventForm))



# since we are doing something very common django has a built in tool to do this for us
class AddEventCreateView(generic.CreateView):
    # using the create view we can just give it the variables 
    # as the functionaity is already built in!
    form_class = CreateEventForm
    template_name = 'eventFinderApp/addevent.html'
    success_url = reverse_lazy('eventFinderApp:index')
    # we have to use reverse_lazy so that urls.py can load our class
    # and not get stuck in a recursive loop 

class EditEventView(generic.UpdateView):
    model = Event
    form_class = CreateEventForm
    success_url = reverse_lazy('eventFinderApp:account')
    template_name = 'eventFinderApp/editevent.html'