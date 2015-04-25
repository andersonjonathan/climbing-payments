from django.shortcuts import render
from .models import *
# Create your views here.
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'payments/index.html'
    context_object_name = 'latest_trips_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Travel.objects.filter(when__lte=timezone.now()).order_by('-when')[:5]


class DetailView(generic.DetailView):
    model = Travel
    template_name = 'payments/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Travel.objects.filter(when__lte=timezone.now())