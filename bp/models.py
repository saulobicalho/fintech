from django.db import models

class balanco_patrimonial(models.Model):
    empresa = models.CharField()
    ano = models.IntegerField()
# Create your models here.
