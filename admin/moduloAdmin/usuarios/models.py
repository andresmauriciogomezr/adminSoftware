from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Administrador(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
