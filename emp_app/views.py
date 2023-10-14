from django.shortcuts import render,HttpResponse
from .models import *
from datetime import datetime
# from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=="POST":
        names=request.POST['name']
        department=int(request.POST['department'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        role=int(request.POST['role'])
        emp=Employee(name=names,salary=salary,bonus=bonus,phone=phone,department_id=department,role_id=role,hire_date=datetime.now())
        emp.save()
        return HttpResponse('Employee added successfully')
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('An Exceptions has been occured!! Employee cannot be added')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_removed=Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse('Employee Removeed Succcessfully')
        except:
            return HttpResponse('Select a valid Employee')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        names=request.POST['name']
        dept=request.POST['department']
        role=request.POST['role']
        emps=Employee.objects.all()
        if names:
            emps=emps.filter(name__icontains=names)
        if dept:
            emps=emps.filter(department__name=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)

        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)    
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An Exceptions has been occured!!')

