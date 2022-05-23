from django.db import models


# Create your models here.
class Owners(models.Model):
    # objects = None
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)


class Animals(models.Model):
    # objects = None
    id = models.AutoField(primary_key=True)
    primeryownerid = models.ForeignKey(Owners, to_field="id", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255, blank=True, null=True)
    breed = models.CharField(max_length=255)
    age = models.EmailField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255)
