from django.urls import path
from employee.views import company

urlpatterns = [
    path('', company, name='employee_list')
]