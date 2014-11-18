# coding=utf-8
from django.db import models

# Create your models here.
from driver.models import Driver
from vehicle.models import Vehicle


class Drive_History(models.Model):
    driver = models.ForeignKey(Driver)
    vehicle = models.ForeignKey(Vehicle)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __unicode__(self):
        return u"คนชับ %s ทะเบียนรถ %s วันที่ %s ถึง %s" % (
            self.driver.user.get_full_name(),
            self.vehicle.license_id,
            self.start_date,
            self.end_date
        )