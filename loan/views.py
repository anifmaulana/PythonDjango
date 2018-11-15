from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Loan
from customer.models import Customer
from customer.models import Customers_rel_loan



def handler404(request):
       return render(request,'404.html',status=404)

def index(request):
       loan = Loan.objects.all()
       #customer = Customers_rel_loan.objects.filter(status='paid').all().select_related('custid').distinct('custid_id')
       customer = Customers_rel_loan.objects.exclude(custid_id__in = Customers_rel_loan.objects.filter(status='onprogres').values_list('custid_id', flat=True)).distinct('custid_id')
       #// make out in HttpResponse
       # output = ', '.join([str(loan) for loan in loans])
       # return HttpResponse(output)
       return render(request,'loan/index.html',{'loan':loan,'customer':customer})

def detail_status(request,id):

       #loans = Loan.objects.all()
       #loan = Loan.objects.get(pk = id)
       loan = get_object_or_404(Loan,pk=id)
       return render(request , 'loan/detail_status.html',{'loan':loan})

def add_status_loan(request,id):
       loan = get_object_or_404(Loan,pk=id)
       if request.method == 'POST':
              addDesc  = request.POST['desc']
              loan.status_loan_set.create(desc = addDesc)
              return HttpResponseRedirect('/loan')

