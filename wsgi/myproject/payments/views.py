from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
from django.views import generic
from .forms import *
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory


class IndexView(generic.ListView):
    template_name = 'payments/index.html'
    context_object_name = 'latest_trips_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Travel.objects.filter(when__lte=timezone.now()).order_by('-when')[:5]


def detail(request, pk ):
    travel = get_object_or_404(Travel, pk=pk)
    i = 0
    for p in Passenger.objects.filter(trip_id = pk):
        i += 1
    costPerPassenger = travel.where.fee / (i+1)
    return render(request, 'payments/detail.html', {'travel': travel, 'costPerPassenger': costPerPassenger})


def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print form['your_name'].value()

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'payments/name.html', {'form': form})


def addPerson(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()
    return render(request, 'payments/addPerson.html', {'form': form})


def addPlace(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PlaceForm()
    return render(request, 'payments/addPlace.html', {'form': form})

from django.forms.formsets import formset_factory


def addTravel(request):
    PassengerFormSet = formset_factory(PassengerForm, extra=4, min_num=1, validate_min=True)
    if request.method == 'POST':
        form = TravelForm(request.POST)
        formset = PassengerFormSet(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            travel = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    passenger = inline_form.save(commit=False)
                    passenger.trip = travel
                    passenger.save()
            return HttpResponseRedirect('/')
    else:
        form = TravelForm()
        formset = PassengerFormSet()

    return render(request, 'payments/addTravel.html', {'form': form, 'formset': formset})