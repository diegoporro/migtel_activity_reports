from django.contrib.admin import ModelAdmin
from django.db import models

# Create your models here.


# Department model
class Department(models.Model):
    DepartmentName = models.CharField(max_length=30, null=False, blank=False)
    DepartmentEmail = models.EmailField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.DepartmentName


class DepartmentAdmin(ModelAdmin):
    list_display = ['DepartmentName', 'DepartmentEmail']
    list_filter = ['DepartmentName', 'DepartmentEmail']


# Employee model
class Employee(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large")
    ]
    DepartmentName = models.ForeignKey(Department, on_delete=models.CASCADE)
    EmployeeName = models.CharField(max_length=60, null=False, blank=False)
    EmployeeCharge = models.CharField(max_length=20, null=False, blank=False)
    EmployeeNumber = models.IntegerField(null=False, blank=False)
    EmployeeEmail = models.EmailField(max_length=100, null=False, blank=False)
    EmployeeCI = models.IntegerField(null=False, blank=False)
    EmployeeRIF = models.CharField(max_length=15, null=False, blank=False)
    EmployeeAddress = models.CharField(max_length=250, null=False, blank=False)
    EmployeeBirthday = models.CharField(max_length=10, null=False, blank=False)
    EmployeeShirtSize = models.CharField(max_length=15, choices=SHIRT_SIZES)
    EmployeeShoesSize = models.IntegerField(null=False, blank=False)
    EmployeePantSize = models.IntegerField(null=False, blank=False)
    EmployeeAdmission = models.CharField(max_length=10, null=False, blank=False)
    EmployeeEmergencyContact = models.CharField(max_length=60, null=False, blank=False)
    EmployeeEmergencyNumber = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.EmployeeName


# Cells model
class Cells(models.Model):
    CITY = [
        ("CCS", "Caracas"),
        ("GUA", "Guatire-Guarenas"),
        ("CAU", "Caucagua"),
        ("HIG", "Higuerote")
    ]
    CellCity = models.CharField(max_length=15, choices=CITY)
    CellName = models.CharField(max_length=60, null=False, blank=False)
    CellAddress = models.CharField(max_length=100, null=False, blank=False)
    CellCoord = models.CharField(max_length=60, null=False, blank=False)
    CellHeight = models.IntegerField(null=False, blank=False)
    CellContact = models.CharField(max_length=60, null=False, blank=False)
    CellContactNumber = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.CellName


# Activity model
class Activity(models.Model):
    ACTIVITY_TYPE = [
        ("SOPORTE", "Soporte"),
        ("INSTALACION", "Instalacion"),
        ("CELDAFULL", "Full dia de celda"),
        ("CELDAMEDIA", "Medio dia de celda")
    ]
    STATUS_TYPE = [
        ("ASIGNADO", "Asignado"),
        ("COMPLETADO", "Completado"),
        ("NO FINALIZADO", "No finalizado")
    ]
    CITY = [
        ("CCS", "Caracas"),
        ("GUA", "Guatire-Guarenas"),
        ("CAU", "Caucagua"),
        ("HIG", "Higuerote")
    ]
    Act = models.CharField(max_length=20, choices=ACTIVITY_TYPE)
    Person1 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Contratis_1')
    Person2 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Contratis_2', null=True, blank=True)
    Person3 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Contratis_3', null=True, blank=True)
    Person4 = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Contratis_4', null=True, blank=True)
    DateAsig = models.CharField(max_length=10, null=False, blank=False)
    DateRes = models.CharField(max_length=10, null=True, blank=True)
    Status = models.CharField(max_length=20, choices=STATUS_TYPE)
    Celda = models.ForeignKey(Cells, on_delete=models.CASCADE)
    Ciudad = models.CharField(max_length=20, choices=CITY)
    Cliente = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.Act


