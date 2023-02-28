from django.contrib import admin
from employee.models import Employee


# Register your models here.
# Register Model in Django Admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "contact",
        "address",
        "salary"
    ]
# Register your models here.
