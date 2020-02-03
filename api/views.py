# Create your views here.

from rest_framework import generics

from ReportSystem.models import Reporter, Crime, Station, Security, Report
from .serializers import ReporterSerializer, CrimeSerializer, StationSerializer, SecuritySerializer, ReportSerializer


class ReporterListView(generics.ListCreateAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class ReporterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class CrimeListView(generics.ListCreateAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer


class CrimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer


class StationListView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class SecurityListView(generics.ListCreateAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class SecurityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
