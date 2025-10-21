from django.urls import path
from employee.views import companies, company_detail

urlpatterns = [
    path('companies/', companies, name='company_list'),
    path('company_detail/<uuid:pk>/', company_detail, name='company_detail')
]