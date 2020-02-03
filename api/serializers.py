from rest_framework import serializers

from ReportSystem.models import Reporter, Crime, Station, Security, Report


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ('id', 'reporter', 'address', 'phone_number', 'created_at')


class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime
        fields = ('id', 'reporter', 'crime_type', 'description', 'location', 'created_at')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'name', 'location', 'created_at')


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('id', 'crime', 'officer', 'address', 'phone_number', 'station', 'created_at')


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'subject', 'details', 'crime', 'reporter', 'security', 'approve', 'status', 'created_at')
