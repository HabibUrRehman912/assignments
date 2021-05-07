from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight,Passenger
# Create your views here.
def index(request):
    return render(request,"hello/index.html",{
        "Flights": Flight.objects.all()
    })

def greet(request,name):
    return HttpResponse(f"Hello {name}")

def flight(request,flight_id):
    flights = Flight.objects.get(pk=flight_id)
    return render(request,"hello/flight.html",{
        "Flights": flights,
        "passengers" : flights.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flights).all()
    })
def book(request,flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passengers']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight_id,)))
        

def hello(request,name):
    return render(request,"hello/greet.html",
    {
        "name": name.capitalize()
    })