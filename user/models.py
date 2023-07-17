from django.db import models

# Create your models here.

class Registration(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField()
	whatsapp_number = models.CharField(max_length=14)
	is_a_member_of_LTA = models.CharField(max_length=4)
	how_did_you_hear_of_us = models.CharField(max_length=30)
	expectations_for_SOTS = models.TextField()
	date_registered = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}'s Profile"

	class Meta:
		ordering = ("-date_registered",)
		verbose_name_plural = 'Registrations'


class Volunteer(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField()
	whatsapp_number = models.CharField(max_length=14)
	age = models.CharField(max_length=2)
	department = models.CharField(max_length=40)
	months_of_experience = models.CharField(max_length=15)
	will_be_available_for_bootcamp = models.CharField(max_length=3)
	is_a_member_of_LTA = models.CharField(max_length=4)
	how_did_you_hear_of_us = models.CharField(max_length=30)
	expectations_for_SOTS = models.TextField()
	date_registered = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}'s Profile"

	class Meta:
		ordering = ("-date_registered",)
		verbose_name_plural = 'Volunteers'

