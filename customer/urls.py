from . import views
from django.urls import path
from django.conf.urls import handler404,handler500

app_name = 'customer'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>', views.detail_loan_customer,name='detail_loan_customer'),
    path('add_user_customer/<int:id>', views.add_user_customer,name='add_user_customer'),
    path('add_repeat_order/<int:id>', views.add_repeat_order,name='add_repeat_order'),
    path('revision_loan', views.revision_loan,name='revision_loan'),
    path('custmer_repeatorder/<int:id>/<int:custid>/', views.custmer_repeatorder,name='custmer_repeatorder')
]

handler404 = 'views.handler404'