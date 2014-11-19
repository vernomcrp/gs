from rest_framework import serializers

from vehicle.models import Vehicle


class VehicleSerializer(serializers.Serializer):
    pk = serializers.Field()
    license_id = serializers.CharField()
    description = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.license_id = attrs.get('license_id', instance.license_id)
            instance.description = attrs.get('description', instance.description)
            return instance
        return Vehicle(**attrs)