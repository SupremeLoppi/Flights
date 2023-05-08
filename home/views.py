from django.shortcuts import render

def index(request):
	return (render(request,"home/index.html"))

def about(request):
	return (render(request,"home/about.html"))
	

def flights(request):
	return (render(request,"home/flights.html"))


def flightdetails(request,pk):
	return (render(request,"home/flightdetails.html"))
	

def citydetails(request,pk):
	return (render(request,"home/citydetails.html"))
