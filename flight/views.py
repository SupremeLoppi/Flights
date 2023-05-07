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