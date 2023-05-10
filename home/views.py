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
	flightcompany=FlightCompany.objects.get(name=flight.owner)

	destination_airport=Airport.objects.get(name=flight.destination)
	departure_airport=Airport.objects.get(name=flight.departure)

	destination_city=City.objects.get(name=destination_airport.location)
	departure_city=City.objects.get(name=departure_airport.location)

	departure_city_id=departure_city.id
	destination_city_id=destination_city.id



	data={
		"flight":flight,
		"flightcompany":flightcompany,
		"destination_city":destination_city,
		"departure_city":departure_city,
		"destination_city_id":destination_city_id,
		"departure_city_id" :departure_city_id
	}
	return (render(request,"home/flightdetails.html",data))
	
def city(request):

	cities=City.objects.all()

	data={
		"cities":cities
	}

	return render(request,"home/cities.html",data)


def citydetails(request,pk):

	city=City.objects.get(id=pk)
	places=Places.objects.filter(location=city)




	data={
		"city":city,
		"places":places
	}

	return (render(request,"home/citydetails.html",data))

def flightcompanydetails(request,pk):
	flightcompany=FlightCompany.objects.get(id=pk)
	data={
		"flightcompany":flightcompany
	}
	return render(request,"home/flightcompanydetails.html",data)