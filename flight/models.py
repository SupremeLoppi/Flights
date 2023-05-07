from django.db import models
# from django.models import models
# Create your models here.


class Cities(models.Model):
	name=models.CharField(max_length=69)

	def __str__(self):
		return f"{self.name}"


class Airport(models.Model):
	title=models.CharField(max_length=69)
	location=models.ForeignKey(Cities,on_delete=models.CASCADE,related_name="airport")


	def __str__(self):
		return f"{self.title}"


class Flight(models.Model):
	departure=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departing_flights")
	destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arriving_flights")
	price=models.IntegerField()

	def __str__(self):
		return f"from {self.departure} to {self.destination}"