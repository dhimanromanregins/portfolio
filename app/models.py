from datetime import datetime
import email
from django.db import models


# Create your models here.


class Info(models.Model):
    name = models.CharField(max_length=255)
    Profile = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.BigIntegerField()

    

class Aboutme(models.Model):
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()


class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    project_date = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    project_description = models.TextField()
    

