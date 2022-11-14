from django.db import models

class familia1(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    