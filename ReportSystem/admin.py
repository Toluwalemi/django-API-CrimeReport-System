from django.contrib import admin

from .models import Reporter, Crime, Station, Security, Report

# Register your models here.

admin.site.register(Reporter)
admin.site.register(Crime)
admin.site.register(Station)
admin.site.register(Security)
admin.site.register(Report)
