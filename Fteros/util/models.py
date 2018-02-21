# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ConnectionSetting(models.Model):

    name = models.CharField(primary_key=True,max_length=20)
    server = models.CharField(max_length=50)
    database = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
