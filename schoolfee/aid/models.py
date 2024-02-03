from django.db import models
from fee.models import Student


class AidName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class FeeAid(models.Model):
    student = models.Foreignkey(Student, on_delete=models.CASCADE)
    Aid_mount = models.PositiveIntegerField()
    Aid_type = models.Foreignkey(AidName, max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "%" % (self.student)
