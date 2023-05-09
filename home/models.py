from django.db import models

# Create your models here.

class Country(models.Model):
	name=models.CharField(max_length=50)

	def __str__(self):
		return f"{self.name}"

class City(models.Model):
	name=models.CharField(max_length=50)
	Country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name="countryx")

	def __str__(self):
		return f"{self.name}"



class Places(models.Model):
	popularity_choices=(
		("high" , "high"),
		("low", "low"),
		("most popular","most popular"),
		("least popular","least popular"),)

	name=models.CharField(max_length=69)
	popularity=models.CharField(max_length=69,choices=popularity_choices)
	location=models.ForeignKey(City,on_delete=models.CASCADE,related_name="city_namep")

	def __str__(self):
		return f"{self.name}"


class FlightCompany(models.Model):
	name=models.CharField(max_length=50)
	descriptions=models.TextField(default='')

	def __str__(self):
		return f"{self.name}"


class Airport(models.Model):
	name=models.CharField(max_length=50)
	location=models.ForeignKey(City,on_delete=models.CASCADE,related_name="city_name")

	def __str__(self):
		return f"{self.name}"

class Flight(models.Model):
	class_choices = (
        ('high class', 'high class'),
        ('middle class', 'middle class'),
        ('business class', 'business class'),
    )

	pricing_choices = (
        (500, '500'),
        (1000, '1000'),
        (800, '800'),
        (300, '300'),
        (200, '200'),

    )

	code=models.CharField(max_length=6)
	owner=models.ForeignKey(FlightCompany,on_delete=models.CASCADE,related_name="flight_company")
	departure=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departurex")
	destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="destinationx")
	pricing=models.IntegerField(choices=pricing_choices)
	duration=models.IntegerField(default=300)
	capacity=models.IntegerField(default=500)
	standard=models.CharField(max_length=50,choices=class_choices)
	
	def __str__(self):
		return f"{self.code}"





