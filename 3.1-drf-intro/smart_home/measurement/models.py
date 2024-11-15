from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True, default=None)


class Measurement(models.Model):
    temperature = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', max_length=150, blank=True, null=True, default=None)

