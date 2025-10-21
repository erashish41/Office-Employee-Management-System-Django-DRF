from django.urls import path
from employee.views import companies

urlpatterns = [
    path('companies/', companies, name='company_list')
]