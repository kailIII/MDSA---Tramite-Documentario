# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Via(models.Model):
	via = models.CharField(max_length=255, unique=True, help_text="Escribir vía.")