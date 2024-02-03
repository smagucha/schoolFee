from django.db import models
from fee.models import Student
from appfee.models import Fee


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    Amount_paid = models.PositiveIntegerField()
    Payment_date = models.DateField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.student)
