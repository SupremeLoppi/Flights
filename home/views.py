from django.shortcuts import render
from .models import *


def index(request):
	return (render(request,"home/index.html"))

def about(request):
	return (render(request,"home/about.html"))
	

def flights(request):
	all_flights=Flight.objects.all()

	data={
		"flights":all_flights,
	}
	return (render(request,"home/flights.html",data))


def flightdetails(request,pk):
	flight=Flight.objects.get(id=pk)
	city=City.objects.get()

	data={
		"flight":flight,
		"city":city
	}
	return (render(request,"home/flightdetails.html",data))
	

def citydetails(request,pk):
	return (render(request,"home/citydetails.html"))
