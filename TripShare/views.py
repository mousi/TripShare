from django.shortcuts import render
from TripShare.models import Trip, TripUser, Request

# Create your views here.
def index(request):

    trips_list = Trip.objects.all()
    request_list = Request.objects.all()
    context_dict = { 'trips':trips_list, 'requests':request_list}
    return render(request, 'index.html', context_dict)

def about(request):
    return render(request, 'about.html', {})

def test(request):
    context_dict = {}
    return render(request, 'test.html', context_dict)