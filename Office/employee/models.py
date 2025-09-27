from django.db import models

# Create your models here.

COMPANY_TYPE = [
    ("it", "IT"),
    ("non-it", "NON_IT")
]

CONTRACT_TYPE = [
    ("full_time", "FULL_TIME"),
    ("part_time", "PART_TIME"),
    ("intern", "INTERN"),
    ("contractor", "CONTRACTOR")
]

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    about = models.TextField()
    company_type = models.CharField(max_length=10,choices= COMPANY_TYPE, default="it")
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} {self.company_type}"
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=5, unique=True)
    project = models.ManyToManyField(Project, related_name="project")
    contract_type = models.CharField(max_length=20,choices=CONTRACT_TYPE, default="full_time")
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    about = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    leaving_date = models.DateField(null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name="employee_department")
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name="employee_company")
    
    def __str__(self):
        return f"{self.first_name} {self.code} {self.joining_date}"