from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer

# Create your views here.


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def vehicle_list(request):
    if request.method == 'GET':
        vehicle_list = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicle_list, many=True)
        return JSONResponse(serializer.data)