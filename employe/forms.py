from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name','email','post','salary')
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'input w-full form-control',
                 'placeholder':'Employee Name'}),
            'email': forms.TextInput(attrs={
                'class': 'input w-full form-control',
                'placeholder': 'Employee Email'}),
            'post': forms.TextInput(attrs={
                'class': 'input w-full form-control',
                'placeholder': 'Employee post'}),
            'salary': forms.TextInput(attrs={
                'class': 'input w-full form-control',
                'placeholder': 'Employee salary'}),
        }