from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Reporter(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporters')
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reporter_id


class Crime(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporters')
    crime_type = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.crime_type


class Station(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]
        ordering = ['-name']

    def __str__(self):
        return self.name


class Security(models.Model):
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='crimes')
    officer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='officers')
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='stations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'security'
        verbose_name_plural = 'securities'

    def __str__(self):
        return self.officer.get_full_name()


class Report(models.Model):
    subject = models.CharField(max_length=30)
    details = models.TextField()
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='crimes')
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, related_name='reporters')
    security = models.ForeignKey(Security, on_delete=models.CASCADE, related_name='securities')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
