from django.contrib import admin
from employee.models import Company, Employee, Project, Department

# Register your models here.

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Department)