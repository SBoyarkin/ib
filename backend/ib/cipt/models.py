from django.db import models


class Certificate(models.Model):
    serial_number = models.CharField(max_length=255)


class Dst(models.Model):
    serial_number = models.CharField(max_length=255)

class Csp(models.Model):
    serial_number = models.CharField(max_length=255)



# Create your models here.
