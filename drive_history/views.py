from django.shortcuts import render

# Create your views here.
from drive_history.models import Drive_History
from rest_framework import viewsets
from rest_framework.response import Response

from drive_history.serializers import DriveHistorySerializer
from rest_framework.decorators import api_view

# class DriveHistoryViewSet(viewsets.ModelViewSet):
#     queryset = Drive_History.objects.all()
#     serializer_class = DriveHistorySerializer

@api_view(['GET', 'POST'])
def drive_history_list(request):
    if request.method == 'GET':
        serializer = DriveHistorySerializer(Drive_History.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DriveHistorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
