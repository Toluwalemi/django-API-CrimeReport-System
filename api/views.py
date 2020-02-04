# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics

from ReportSystem.models import Reporter, Crime, Station, Security, Report
from .permissions import IsReporterOrReadOnly
from .serializers import ReporterSerializer, CrimeSerializer, StationSerializer, SecuritySerializer, ReportSerializer, \
    UserSerializer


class ReporterListView(generics.ListCreateAPIView):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class ReporterDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReporterOrReadOnly,)
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CrimeListView(generics.ListCreateAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer


class CrimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReporterOrReadOnly,)
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer


class StationListView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReporterOrReadOnly,)
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class SecurityListView(generics.ListCreateAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class SecurityDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReporterOrReadOnly,)
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReporterOrReadOnly,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
