from django.db import models
from loan.models import Loan

class Customer(models.Model):
       GENDER_CHOICES = (
                             ('M', 'Male'),
                             ('F', 'Female'),
                            )
       gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
       first_name = models.CharField(max_length=15)
       last_name = models.CharField(max_length=15)
       email = models.CharField(max_length=50)
       password = models.TextField()
       date_birth = models.DateField()
       phone= models.CharField(max_length=20)
       npwp= models.CharField(max_length=20)
       ktp=  models.CharField(max_length=20)

class Customers_rel_loan(models.Model):
       custid   = models.ForeignKey(Customer,on_delete=models.CASCADE)
       loanid    = models.ForeignKey(Loan,on_delete=models.CASCADE)
       loans     = models.IntegerField()
       time_period = models.IntegerField(default=None, blank=True, null=True)
       interest_rate = models.FloatField(default=None, blank=True, null=True)
       installment = models.IntegerField(default=None, blank=True, null=True)
       interest_monthly = models.IntegerField(default=None, blank=True, null=True)
       status = models.CharField(max_length=10,default=None, blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add = True)


