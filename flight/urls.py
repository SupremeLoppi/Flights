from django.urls import path
from . import views

urlpatterns=[
	path("",views.flightindex,name="flightindex"),
	path("city",views.city_and_airport,name="cityindex"),
	path("detail/<int:id>",views.detail,name="detail")


]