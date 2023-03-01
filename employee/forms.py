from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'id': forms.TextInput(attrs={
                'class': "data",
                'placeholder': 'Enter your id here'
                }),
            'name': forms.TextInput(attrs={
                'class': "data",
                'placeholder': 'Enter your name here'
                }),
            'email': forms.EmailInput(attrs={
                'class': "data",
                'placeholder': 'Enter your email here'
                }),
            'contact': forms.TextInput(attrs={
                'class': "data",
                'placeholder': 'Enter your Mobile Number here'
                }),
            'address': forms.TextInput(attrs={
                'class': "data",
                'placeholder': 'Enter your Address here'
                }),
            'salary': forms.TextInput(attrs={
                'class': "data",
                'placeholder': 'Enter your Salary here'
                })
        }
