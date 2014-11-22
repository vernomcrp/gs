from rest_framework import serializers

from vehicle.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    route_paths = serializers.RelatedField(many=True)
    drive_by = serializers.RelatedField()

    class Meta:
        model = Vehicle
        fields = ('license_id', 'description', 'drive_by', 'route_paths')
