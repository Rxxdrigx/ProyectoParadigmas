from pyexpat import model
from django.db import models

# Create your models here.
class Applicants(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)