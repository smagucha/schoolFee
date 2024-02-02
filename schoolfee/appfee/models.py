from django.db import models


class Term(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class Fee(models.Model):
    fee_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    Amount = models.PositiveIntegerField()
    DueDate = models.DateField()
    Grade = models.CharField(max_length=100)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.fee_name)
