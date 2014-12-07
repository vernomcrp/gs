from rest_framework import serializers
from drive_history.models import Drive_History


class DriveHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive_History
        fields = ('id', 'latitude', 'longitude', 'created_date', 'last_modified', 'driver', 'vehicle')