from django.db import models

# Create your models here.


class user(models.Model):
    regno = models.BigIntegerField()
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=6)
    course = models.CharField(max_length=50)
    batch = models.IntegerField()
    dept = models.CharField(max_length=3)
    section = models.CharField(max_length=3)
