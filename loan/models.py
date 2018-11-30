from django.db import models

class Loan(models.Model):
       title = models.CharField(max_length = 100)
       desc = models.TextField()
       created_at = models.DateTimeField(auto_now_add = True)

class status_loan(models.Model):
       status  = models.ForeignKey(Loan,on_delete=models.CASCADE)
       desc    = models.TextField()
       created_at = models.DateTimeField(auto_now_add = True)

