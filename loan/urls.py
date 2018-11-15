from . import views
from django.urls import path
from django.conf.urls import handler404,handler500

app_name = 'loan'
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>', views.detail_status,name='detail_status'),
    path('add_status_loan/<int:id>', views.add_status_loan,name='add_status_loan'),
]

handler404 = 'views.handler404'