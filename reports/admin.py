from django.contrib import admin
from .models import *


class DepartmentAdmin(ModelAdmin):
    list_display = ['DepartmentName', 'DepartmentEmail']
    list_filter = ['DepartmentName', 'DepartmentEmail']


class EmployeeAdmin(ModelAdmin):
    list_display = ['EmployeeName', 'EmployeeCI', 'EmployeeEmail']
    list_filter = ['EmployeeName', 'EmployeeCI', 'EmployeeEmail']


class CellsAdmin(ModelAdmin):
    list_display = ['CellCity', 'CellName', 'CellAddress']
    list_filter = ['CellCity', 'CellName', 'CellAddress']


class ActivityAdmin(ModelAdmin):
    list_display = ['Act', 'Celda', 'Ciudad', 'Status', 'Ciudad']
    list_filter = ['Act', 'Celda', 'Ciudad', 'Status', 'Ciudad']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Cells, CellsAdmin)
admin.site.register(Activity, ActivityAdmin)

# Register your models here.
