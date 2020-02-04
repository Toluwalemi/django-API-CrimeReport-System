from django.urls import path

from .views import ReporterListView, ReporterDetailView, CrimeListView, StationListView, StationDetailView, \
    SecurityListView, SecurityDetailView, ReportListView, ReportDetailView, CrimeDetailView

urlpatterns = [
    path('v1', ReporterListView.as_view()),
    path('v1/<int:pk>/', ReporterDetailView.as_view()),

    path('v2', CrimeListView.as_view()),
    path('v2/<int:pk>/', CrimeDetailView.as_view()),

    path('v3', StationListView.as_view()),
    path('v3/<int:pk>/', StationDetailView.as_view()),

    path('v4', SecurityListView.as_view()),
    path('v4/<int:pk>/', SecurityDetailView.as_view()),

    path('v5', ReportListView.as_view()),
    path('v5/<int:pk>/', ReportDetailView.as_view()),

]
