from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee
from .forms import EmployeeForm


def liste_employee(request):
    employes = Employee.objects.all()
    return render(request, 'employe/liste_employee.html', {'employes': employes})


def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employe/add_employee.html', {'form': form})


def modify_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employe/add_employee.html', {'form': form})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employe/delete.html', {'employee': employee})