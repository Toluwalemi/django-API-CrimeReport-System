from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    # phone_number
#   usertype


class Crime(models.Model):
    # crime_type =
    # user foreign key
    subject = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # progress_note = models.


class Station(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=50)


class Security(models.Model):
    # crime_id foreign key
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    # password
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Report(models.Model):
    report_type = models.CharField(max_length=30)
    details = models.TextField()
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
