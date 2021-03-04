from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  is_visitor = models.BooleanField(default=False)
  is_practitioner = models.BooleanField(default=False)

class Visitor(models.Model):
    visitor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    GENDER = [
       ('M', 'Male'),
       ('F', 'Female'),
       ('N', 'Other')
    ]
    addressline1 = models.CharField(max_length=100)
    addressline2 = models.CharField(max_length=100)
    postal_code= models.IntegerField()
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    gender = models.CharField(
        max_length=20,
        choices=GENDER,
        default='M',
    )
    dob = models.DateField(max_length=8)

    
    def __str__(self):
        return self.visitor.username

class Practitioner(models.Model):
    practitioner = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.practitioner.username
