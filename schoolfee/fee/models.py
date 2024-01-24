from django.db import models


class Student(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Grade = models.CharField(max_length=100)
    GuardianorparentContactInfo = models.CharField(max_length=100)
