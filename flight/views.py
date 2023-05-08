from django.shortcuts import render
from .models import Cities,Airport,Flight


# Create your views here.

def flightindex(request):
	flights=Flight.objects.all()

	data={"flights":flights}


	return render(request,"flight/flightindex.html",data)

def city_and_airport(request):
	cities=Cities.objects.all()
	airports=Airport.objects.all()



	data={"city":cities,"airports":airports}

	return render(request,"flight/cityandairport.html",data)


def detail(request,pk):
	flight=Flight.objects.get(id=pk)
	departure_airport=flight.departure
	destination_airport=flight.destination

	departure_city=Airport.objects.get(title=departure_airport).location
	destination_city=Airport.objects.get(title=destination_airport).location


	data={"id":pk,"flight":flight,"departure":departure_airport,"destination":destination_airport,
		"destination_city":destination_city,"departure_city":departure_city}
	return render(request,"flight/details.html",data)