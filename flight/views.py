from django.shortcuts import render

# Create your views here.

def flightindex(request):

	return render(request,"flight/flightindex.html")