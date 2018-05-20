from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SEX = (
	('M','Male'),
	('F','Female'),
	('O','Others'),
	)

TYPE = (
	('1','Employee'),
	('2','Employer'),
	('3','Admin'),
	)

class UserProfile(models.Model):
	user_name  = models.CharField(max_length=50,unique=True)
	first_name = models.CharField(max_length=50,null=False)
	last_name  = models.CharField(max_length=50,null=False)
	password   = models.CharField(max_length=25,null=False)
	email      = models.EmailField(max_length=254,unique=True,null=False)
	contact    = models.CharField(max_length=15,null=False)
	dob        = models.DateTimeField(default=None,null=False)
	sex        = models.CharField(max_length=6,choices=SEX,null=False)
	userType   = models.CharField(max_length=10,choices=TYPE,default='1')


