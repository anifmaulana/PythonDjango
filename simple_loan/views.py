from django.shortcuts import render
from django.http import HttpResponse
from loan.models import Loan
from customer.models import Customer
from customer.models import Customers_rel_loan
from django.db.models import Sum

def dashboard(request):
       actif_cust = Customers_rel_loan.objects.filter(status='onprogres').count()
       nonactif_cust = Customers_rel_loan.objects.filter(status='paid').count()
       sum_onprogres = Customers_rel_loan.objects.filter(status='onprogres').aggregate(Sum('loans'))
       sum_paid = Customers_rel_loan.objects.filter(status='paid').aggregate(Sum('loans'))
       #return HttpResponse(count_cust)
       return render(request,'dashboard.html',{'actif_cust':actif_cust,'nonactif_cust':nonactif_cust,'sum_onprogres':sum_onprogres,'sum_paid':sum_paid})