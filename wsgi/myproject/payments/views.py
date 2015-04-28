# coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here
from django.views import generic
from .forms import *
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout

from django.forms.formsets import formset_factory


def loginView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    # Return a 'disabled account' error message
                    return HttpResponseRedirect('/login/')
            else:
                # Return an 'invalid login' error message.
                return HttpResponseRedirect('/login/')
        else:
            return render(request, 'payments/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

class IndexView(generic.ListView):
    template_name = 'payments/index.html'
    context_object_name = 'latest_trips_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Travel.objects.filter(when__lte=timezone.now()).order_by('-when')


def detail(request, pk ):
    travel = get_object_or_404(Travel, pk=pk)
    costPerPassenger = travel.costPerPassenger(pk)
    return render(request, 'payments/detail.html', {'travel': travel, 'costPerPassenger': costPerPassenger})


def addPerson(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = PersonForm()
        return render(request, 'payments/addPerson.html', {'form': form})
    else:
        return render(request, 'payments/login.html')


def addPlace(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PlaceForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = PlaceForm()
        return render(request, 'payments/addPlace.html', {'form': form})
    else:
        return render(request, 'payments/login.html')




def addTravel(request):
    if request.user.is_authenticated():
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
                        mytrip = MyTrip(person=passenger.name, trip=travel, isPayed=False, cost=0)
                        mytrip.save()
                costPerPassenger = travel.costPerPassenger(travel.id)
                cost = 0
                for p in MyTrip.objects.filter(trip_id = travel.id):
                    p.cost = costPerPassenger
                    p.save()
                    cost = cost + costPerPassenger
                mytrip = MyTrip(person=travel.driver, trip=travel, isPayed=False, cost=(0 - cost))
                mytrip.save()
                return HttpResponseRedirect('/')
        else:
            form = TravelForm()
            formset = PassengerFormSet()

        return render(request, 'payments/addTravel.html', {'form': form, 'formset': formset})
    else:
        return render(request, 'payments/login.html')


class PersonView(generic.ListView):
    template_name = 'payments/persons.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Person.objects.all


def pay(request, pk):
    if request.user.is_authenticated():
        person = get_object_or_404(Person, pk=pk)
        trips = MyTrip.objects.filter(isPayed=False, person_id=pk)
        payedTrips = MyTrip.objects.filter(isPayed=True, person_id=pk)
        totalcost = {}
        driver = {}
        for t in trips:
            if t.trip.driver.name in totalcost:
                totalcost[t.trip.driver.name] = totalcost[t.trip.driver.name] + t.cost
            else:
                totalcost[t.trip.driver.name] = t.cost
                driver[t.trip.driver.name] = t.trip.driver
        print(totalcost)
        return render(request, 'payments/pay.html', {'person': person, 'trips':trips, 'toPay':totalcost, 'driver':driver, 'payedTrips':payedTrips})
    else:
        return render(request, 'payments/login.html')


def hasPayed(request, pk, did):
    if request.user.is_authenticated():
        get_object_or_404(Person, pk=pk)
        get_object_or_404(Person, pk=did)
        trips = MyTrip.objects.filter(person_id=pk, isPayed=False)
        paydate = timezone.now()
        for t in trips:
            if str(t.trip.driver.id) == did:
                t.isPayed = True
                t.payDate = paydate
                t.save()
                trip = MyTrip.objects.filter(person_id=did, trip=t.trip_id)[0]
                trip.cost = trip.cost + t.cost
                if trip.cost == 0:
                    trip.isPayed = True
                trip.save()
        return HttpResponseRedirect('/person/' + pk + '/')
    else:
        return render(request, 'payments/login.html')