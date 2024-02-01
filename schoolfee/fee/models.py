from django.db import models


class Student(models.Model):
    from datetime import date

    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Grade = models.CharField(max_length=100)
    GuardianorparentContactInfo = models.CharField(max_length=100)
    year = models.CharField(
        max_length=100, blank=True, null=True, default=str(date.today().year)
    )

    def __str__(self):
        return "%s %s" % (self.FirstName, self.LastName)
