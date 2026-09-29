from django import forms
from .models import Department, Designation, Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'