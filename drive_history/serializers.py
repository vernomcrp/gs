from rest_framework import serializers
from drive_history.models import Drive_History


class DriveHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive_History
        fields = ('latitude', 'longitude', 'start_date', 'end_date')