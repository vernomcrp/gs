# coding=utf-8
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    driver_license_id = models.TextField()

    def __unicode__(self):
        return u"ชื่อนามสกุล %s" % self.user.get_full_name()