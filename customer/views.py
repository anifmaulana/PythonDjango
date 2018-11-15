from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from loan.models import Loan
from . models import Customer
from . models import Customers_rel_loan


def handler404(request):
       return render(request,'404.html',status=404)

def index(request):
       Customers_rel_loan_cust = Customers_rel_loan()
       customer     = Customer.objects.all()
       rel_customer = Customers_rel_loan.objects.filter(custid_id__in=customer).select_related()
       #// make out in HttpResponse
       # output = ', '.join([str(loan) for loan in loans])
       return render(request,'customer/index.html',{'customer':customer,'rel_customer':rel_customer})


def detail_loan_customer(request,id):
       Customers_rel_loan_cust = Customers_rel_loan()
       customer        = Customer.objects.filter(id=id)
       loan            = Customers_rel_loan.objects.filter(custid=id).all().select_related('custid').select_related('loanid')
       # thumbnail_list = []
       # for l in loan:
       #     l_info = {}
       #     l_info['title_loan'] = l.title
       #     thumbnail_list.append(l_info)
       # for l in loans:
       #     xa = {}
       #     xa['loans'] = l
       #     thumbnail_list.append(xa)
       # zipped = [list(t) for t in zip(loan, loans)]
       #loan.append(loans)
       # for l in loan:
       #     print (l.title)
       #rel_customer = Customers_rel_loan.objects.filter(custid_id__in=customer).select_related()
       #loanid = Customers_rel_loan.objects.filter(custid_id__in=18).select_related()
       #return HttpResponse(loan)
       return render(request,'customer/detail_loan.html',{'loan':loan,'customer':customer})

def add_user_customer(request,id):
       # print('OKE')
       customer = Customer()
       customers_rel_loan = Customers_rel_loan()
       loan = Loan()
       if request.method == 'POST':
              if request.POST['jangka_waktu'] == 36:
                     jangka_waktu = 3
              elif request.POST['jangka_waktu'] == 24:
                     jangka_waktu = 2
              else :
                     jangka_waktu = 1
              customer.first_name  = request.POST['first_name']
              customer.last_name = request.POST['last_name']
              customer.gender = request.POST['gender']
              customer.date_birth = request.POST['birthdate']
              customer.phone = request.POST['phone']
              customer.ktp = request.POST['ktp']
              customer.npwp = request.POST['npwp']
              customer.email = request.POST['email']
              customer.save()

              customers_rel_loan.custid_id = customer.id
              customers_rel_loan.loanid_id = id
              customers_rel_loan.status = 'onprogres'
              customers_rel_loan.loans = request.POST['jumlah_pinjaman']
              customers_rel_loan.interest_rate = request.POST['bunga']
              customers_rel_loan.time_period = request.POST['jangka_waktu']
              customers_rel_loan.interest_monthly = ((int(request.POST['jumlah_pinjaman']) * float(request.POST['bunga']) * jangka_waktu) / int(request.POST['jangka_waktu']) )/100
              customers_rel_loan.installment = (int(request.POST['jumlah_pinjaman']) / int(request.POST['jangka_waktu']))+ customers_rel_loan.interest_monthly
              customers_rel_loan.save()
              return HttpResponseRedirect('/loan')

def add_repeat_order(request,id):
       # print('OKE')
       customer = Customer()
       customers_rel_loan = Customers_rel_loan()
       loan = Loan()
       if request.method == 'POST':
              if request.POST['jangka_waktu'] == 36:
                     jangka_waktu = 3
              elif request.POST['jangka_waktu'] == 24:
                     jangka_waktu = 2
              else :
                     jangka_waktu = 1

              customers_rel_loan.custid_id = request.POST['custid']
              customers_rel_loan.loanid_id = id
              customers_rel_loan.status = 'onprogres'
              customers_rel_loan.loans = request.POST['jumlah_pinjaman']
              customers_rel_loan.interest_rate = request.POST['bunga']
              customers_rel_loan.time_period = request.POST['jangka_waktu']
              customers_rel_loan.interest_monthly = ((int(request.POST['jumlah_pinjaman']) * float(request.POST['bunga']) * jangka_waktu) / int(request.POST['jangka_waktu']) )/100
              customers_rel_loan.installment = (int(request.POST['jumlah_pinjaman']) / int(request.POST['jangka_waktu']))+ customers_rel_loan.interest_monthly
              customers_rel_loan.save()
              return HttpResponseRedirect('/loan')

def revision_loan(request):
       customers_rel_loan = Customers_rel_loan()
       id = request.POST['id']
       if request.POST.get('jangka_waktu') == 36:
              jangka_waktu = 3
       elif request.POST.get('jangka_waktu') == 24:
              jangka_waktu = 2
       else :
              jangka_waktu = 1
       custid     = request.POST.get('customer_id')
       cust       = Customers_rel_loan.objects.get(id=id)
       cust.loans = request.POST.get('jumlah_pinjaman')
       cust.interest_rate = request.POST.get('bunga')
       cust.time_period = request.POST.get('jangka_waktu')
       cust.status = request.POST.get('status')
       cust.interest_monthly = ((int(request.POST.get('jumlah_pinjaman')) * float(request.POST.get('bunga')) * jangka_waktu) / int(request.POST.get('jangka_waktu')) )/100
       cust.installment = (int(request.POST.get('jumlah_pinjaman')) / int(request.POST.get('jangka_waktu')))+ cust.interest_monthly

       cust.save()

       return HttpResponseRedirect('/customer/'+custid)

def custmer_repeatorder(request,id,custid):
       customer        = Customer.objects.filter(id=custid)
       #return HttpResponse(customer)
       return render(request,'customer/repeat_order.html',{'customer':customer,'loanid':id})



