from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100, blank=True, unique=True),
    age= models.IntegerField( blank=True)
    city= models.CharField(max_length=100, blank=True)

class Status(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    verified= models.BooleanField(max_length=100, blank=True)