from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Reporter(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='reporters')
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.reporter_id)


class Crime(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    crime_type = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.crime_type


class Station(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]
        ordering = ['-name']  # descending order

    def __str__(self):
        return self.name


class Security(models.Model):
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='crimes')
    officer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='officers')
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14, unique=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='stations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'security'
        verbose_name_plural = 'securities'

    def __str__(self):
        return self.officer.get_full_name()


class ApprovedManager(models.Manager):
    """function to return all approved reports"""

    def get_queryset(self):
        return super(ApprovedManager, self).get_queryset().filter(status='STATUS_APPROVE')


class Report(models.Model):
    STATUS_PROCESS = 'P'
    STATUS_FAIL = 'F'
    STATUS_APPROVE = 'A'
    STATUS_CHOICES = [
        (STATUS_PROCESS, 'Processing'),
        (STATUS_FAIL, 'Failed'),
        (STATUS_APPROVE, 'Approved'),
    ]
    subject = models.CharField(max_length=30)
    details = models.TextField()
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    approve = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PROCESS)
    objects = models.Manager()  # The default manager
    approved = ApprovedManager()  # My custom manager

    def __str__(self):
        return self.subject
