from django.db import models


class Modelo(models.Model):
    campo = models.CharField(max_length=100, name='campo')
