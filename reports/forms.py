from django import forms
from django.contrib.auth import (authenticate, get_user_model)
from .models import *


User = get_user_model()
# app = Aplicacion.nombreAplicacion


def my_cities():
    cells = Cells.objects.all()

    choices = []
    for foo in cells:
        choices.append((foo.CellCity, foo.CellCity))

    return choices


def my_cells():
    cells = Cells.objects.all()

    choices = []
    for foo in cells:
        choices.append((foo.CellName, foo.CellName))

    return choices


def my_activities():
    cells = Activity.objects.all()

    choices = []
    for foo in cells:
        choices.append((foo.Act, foo.Act))

    return choices


def my_employees():
    cells = Employee.objects.all()

    choices = []
    for foo in cells:
        choices.append((foo.EmployeeName, foo.EmployeeName))

    return choices


# Formulario de Login
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Wrong password or inexist user")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong password or inexist user")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean()


# Formulario de Asignacion de Actividades
class AssignmentActivityForm(forms.Form):
    Activity = forms.ChoiceField(choices=my_activities(), label='Actividad', widget=forms.Select(attrs={'class': 'form-control', 'style': 'text-shadow: 1px 1px 1px lightgray'}))
    City = forms.ChoiceField(choices=my_cities(), label='Ciudad' ,widget=forms.Select(attrs={'class': 'form-control', 'style': 'text-shadow: 1px 1px 1px lightgray'}))
    Cell = forms.ChoiceField(choices=my_cells(), label='Celda', widget=forms.Select(attrs={'class': 'form-control', 'style': 'text-shadow: 1px 1px 1px lightgray'}))
    Personal1 = forms.ChoiceField(choices=my_employees(), label='Empleado', widget=forms.Select(attrs={'class': 'form-control', 'style': 'text-shadow: 1px 1px 1px lightgray'}))
    Personal2 = forms.ChoiceField(choices=my_employees(), label='Empleado', widget=forms.Select(attrs={'class': 'form-control', 'style': 'text-shadow: 1px 1px 1px lightgray'}), required=False)
    Personal3 = forms.ChoiceField(choices=my_employees(), label='Empleado', widget=forms.Select(attrs={'class': 'form-control', 'style': 'text-shadow: 1px 1px 1px lightgray'}), required=False)
    Personal4 = forms.ChoiceField(choices=my_employees(), label='Empleado', widget=forms.Select(attrs={'class': 'form-control', 'style': 'text-shadow: 1px 1px 1px lightgray'}), required=False)
    Cliente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente...', 'style': 'text-shadow: 1px 1px 1px lightgray'}), label='Cliente')
    Message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Indicaciones para el personal tecnico...', 'style': 'text-shadow: 1px 1px 1px lightgray'}), label='Empleado')

    def clean(self):
        Activity = self.cleaned_data.get("Activity")
        Cells = self.cleaned_data.get("Cells")
        Personal1 = self.cleaned_data.get("Personal1")
        Personal2 = self.cleaned_data.get("Personal2") or None
        Cliente = self.cleaned_data.get("Cliente")
        Personal3 = self.cleaned_data.get("Personal3") or None
        Personal4 = self.cleaned_data.get("Personal4") or None
        Message = self.cleaned_data.get("Message")

        return super(AssignmentActivityForm, self).clean()
