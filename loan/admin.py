from django.contrib import admin
from .models import Loan,status_loan

#OneToMany - Relationship
class Status_loanInline(admin.StackedInline):
       model = status_loan

class LoanAdmin(admin.ModelAdmin):
       inlines = [Status_loanInline, ]

# Register your models here.
admin.site.register(Loan,LoanAdmin)
#admin.site.register(status_loan)