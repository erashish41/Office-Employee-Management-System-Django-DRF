from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Company, Employee, Project, Department

# Create your views here.

def company(request):
    return render(request, 'base.html')