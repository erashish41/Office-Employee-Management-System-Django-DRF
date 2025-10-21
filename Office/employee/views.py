from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Company, Employee, Project, Department
# from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.

print("employee views loaded 1")
def companies(request):
    print("all companies data")
    companies = Company.objects.all()
    context = {'all_companies' : companies}
    return render(request, "company_list.html", context)

print("employee views loaded 2")
def company_detail(request, pk):
    print("company details")
    company = Company.objects.get(id=pk)
    context = {'company': company}
    return render(request, "company_detail.html", context)