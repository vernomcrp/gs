from django.shortcuts import render

# Create your views here.
from drive_history.models import Drive_History
from rest_framework import viewsets

from drive_history.serializers import DriveHistorySerializer


class DriveHistoryViewSet(viewsets.ModelViewSet):
    queryset = Drive_History.objects.all()
    serializer_class = DriveHistorySerializer