from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class JobSeekr(models.Model):
	"""docstring for JobSeekr"""

	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')
			
		