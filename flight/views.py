from django.shortcuts import render


# Create your views here.
def flight(request):
	return render(request,"flight/flightindex.html")