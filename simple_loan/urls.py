from . import views
from django.contrib import admin
from django.urls import include,path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.dashboard),
    #path('loan/',include('loan.urls'),namespace='loan'),
    path('customer/',include('customer.urls',namespace='customer')),
    path('loan/',include('loan.urls',namespace='loan')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
