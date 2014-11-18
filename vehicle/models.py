# coding=utf-8
from django.db import models

# Create your models here.
from driver.models import Driver


class Vehicle(models.Model):
    license_id = models.TextField(verbose_name=u"เลขทะเบียน", null=False, blank=False)
    description = models.TextField(verbose_name=u"รายละเอียดเพิ่มเติม", null=True, blank=True)
    drive_by = models.ForeignKey(Driver, verbose_name=u"ขับโดย")

    def __unicode__(self):
        return u"ทะเบียนรถ %s"