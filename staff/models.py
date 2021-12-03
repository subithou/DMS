from django.db import models


# Create your models here.
class profile(models.Model):
    Faculty_unique_id = models.CharField(max_length=50, primary_key=True)
    Profile_photo = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Date_of_Birth = models.DateField()
    Aadhar_No = models.PositiveIntegerField()
    Caste = models.CharField(max_length=20)
    Religion = models.CharField(max_length=20)
    category =  models.CharField(max_length=25)
    PAN =   models.CharField(max_length=25)
    Date_of_Joining = models.DateField()
    AICTE_unique_Id = models.CharField(max_length=25)
    Appointment_type = models.CharField(max_length=25)
    Cadre = models.CharField(max_length=25)
    Designation = models.CharField(max_length=25)
    Specialisation = models.CharField(max_length=50)
    Department_of_program = models.CharField(max_length=50)
    Examiner_institution = models.CharField(max_length=50)
    Area_of_Research = models.CharField(max_length=50)