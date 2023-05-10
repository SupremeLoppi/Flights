from django.urls import path
from . import views

urlpatterns=[
	path("",views.index,name="index"),
	path("about/",views.about,name="about"),
	path("flights/",views.flights,name="flightlists"),
	path("flights/<int:pk>",views.flightdetails,name="flightdetails"),
	path("city",views.city,name="city"),
	path("city/<int:pk>",views.citydetails,name="citydetails"),
	path("flightcompany/<int:pk>",views.flightcompanydetails,name="flightcompanies"),

]