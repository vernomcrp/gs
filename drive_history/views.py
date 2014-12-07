# Create your views here.
from drive_history.models import Drive_History
from rest_framework.response import Response

from drive_history.serializers import DriveHistorySerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def drive_history_list(request, vehicle=None):
    if request.method == 'GET':
        if vehicle is not None:
            drive_histories = Drive_History.objects.filter(vehicle=vehicle).latest('created_date')
            serializer = DriveHistorySerializer(drive_histories)
        else:
            drive_histories = Drive_History.objects.all()
            serializer = DriveHistorySerializer(drive_histories, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DriveHistorySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
