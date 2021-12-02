from django.db import models


# Create your models here.
class profile(models.Model):
    Name = models.CharField(max_length=50)
    Faculty_unique_id = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Date_of_Birth = models.DateField
    Aadhar_No = models.PositiveIntegerField
