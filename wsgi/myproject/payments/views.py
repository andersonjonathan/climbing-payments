from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
from django.views import generic


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
