from django.db import models

# Create your models here.


class Ping(models.Model):
    hostname = models.CharField(max_length=10)
    connected = models.BooleanField(default=False)
    avg_time = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add=True)
