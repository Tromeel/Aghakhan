from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    medical_history =models.TextField()
    dob = models.DateField()

    def __str__(self):
         return self.firstname + " " + self.lastname

class Doctor(models.Model):
    fullname = models.CharField(max_length=100)
    doctorId = models.IntegerField
    age =models.IntegerField()
    department= models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

class Ward(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    department = models.CharField(max_length=100)
    floor = models.IntegerField()

    def __str__(self):
        return self.name