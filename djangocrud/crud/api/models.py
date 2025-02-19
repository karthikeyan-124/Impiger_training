from django.db import models
from django.template.defaultfilters import length


class User(models.Model):
    age = models.IntegerField()
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name
