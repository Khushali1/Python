from django.db import models


# Create your models here.


class Period(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Member(models.Model):
    period = models.ManyToManyField(Period)
    index = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=50, default='America/Los_Angeles')

    def __str__(self):
        return self.real_name
