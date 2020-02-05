from django.db import models

# Create your models here.

class jobRegister(models.Model):
    position = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Deadline = models.DateField(auto_now_add=True)
    Days = models.CharField(max_length=200)

