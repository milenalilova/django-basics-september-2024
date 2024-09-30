from django.shortcuts import render, redirect

from formsBasics.employees.forms import EmployeeForm, DepartmentForm, SelectOptionForm, CheckboxForm
from formsBasics.employees.models import Department


def index(request):
    select_option_form = SelectOptionForm()
    checkbox_form = CheckboxForm()

    context = {
        'select_option_form': select_option_form,
        'checkbox_form': checkbox_form,
    }

    return render(request, 'employees/home-page.html', context)


def show_departments_list(request):
    return render(request, 'employees/departments-list.html')


def show_employees_list(request):
    return render(request, 'employees/employees-list.html')


def create_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departments list')

    context = {'form': form}

    return render(request, 'employees/create-department.html', context)


def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employees list')

    context = {'form': form}

    return render(request, 'employees/create-employee.html', context)
