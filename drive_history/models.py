# coding=utf-8
from django.db import models

# Create your models here.
from driver.models import Driver
from vehicle.models import Vehicle


class Drive_History(models.Model):
    driver = models.ForeignKey(Driver)
    vehicle = models.ForeignKey(Vehicle, related_name='route_paths')
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"driver(%s),license(%s), position(%s,%s), created(%s), last_modified(%s)" % (
            self.driver.user.get_full_name(),
            self.vehicle.license_id,
            self.latitude,
            self.longitude,
            self.created_date,
            self.last_modified
        )

    class Meta:
        ordering = ('-created_date',)
        get_latest_by = ('created_date',)
