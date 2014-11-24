from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def vehicle_list(request):
    if request.method == 'GET':
        vehicle_list = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicle_list, many=True)
        return Response(serializer.data)
    else:
        serializer = VehicleSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
