from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import (authenticate, login, logout, )
from django.contrib.auth.decorators import login_required
import time
from django.db.models import *
import datetime
import calendar
from django.http import HttpResponse
from django.db.models.functions import Cast
from datetime import date
from django.contrib.auth.decorators import user_passes_test
# import psutil as p
from django.http import JsonResponse


# #Controlador Home
def home(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:
        return redirect('/login/')


# #Controlador Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')

    print('User Authentication: ', request.user.is_authenticated)
    title = "Login"
    form = UserLoginForm(request.POST or None)
    localtime = time.asctime(time.localtime(time.time()))

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated)
        print(username)
        return redirect('/dashboard/')
    return render(request, 'login.html', {"form": form, "title": title, "localtime": localtime})


@login_required(login_url='logout')
def dashboard(request):
    title = "Dashboard"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    print('User: ', current_user.id)
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    print('Last login: ', last_login)
    soportes = Activity.objects.filter(Act='SOPORTE').count()
    inst = Activity.objects.filter(Act='INSTALACION').count()
    print(soportes)
    return render(request, 'dashboard.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname, "soportes": soportes, "inst": inst})


# #Controlador de Logs
# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='logout')
def logs(request):
    title = "POS Logs"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login

    return render(request, 'logs.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname})

# #Controlador de Intranet
# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='logout')
def intranet(request):
    title = "Intranet"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    departamentos = Department.objects.all()
    print(departamentos)
    direccion = Employee.objects.filter(DepartmentName=departamentos[0])
    tech = Employee.objects.filter(DepartmentName=departamentos[1])
    ing = Employee.objects.filter(DepartmentName=departamentos[2])
    admin = Employee.objects.filter(DepartmentName=departamentos[3])
    soporte = Employee.objects.filter(DepartmentName=departamentos[4])
    ventas = Employee.objects.filter(DepartmentName=departamentos[5])
    rrhh = Employee.objects.filter(DepartmentName=departamentos[6])
    fo = Employee.objects.filter(DepartmentName=departamentos[8])
    contratistas = Employee.objects.filter(DepartmentName=departamentos[7])



    # rrhh = Employee.objects.filter(DepartmentName='Recursos Humanos')
    # contratistas = Employee.objects.filter(DepartmentName='Contratistas')

    return render(request, 'intranet.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname, "direccion": direccion,
                   "ventas": ventas, "ing": ing, "fo": fo, "admin": admin, "soporte": soporte,
                   "tech": tech,"rrhh": rrhh, "contratistas": contratistas
                   })

# #Controlador de Departamentos
# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='logout')
def departments(request):
    title = "Departamentos"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    departments = Department.objects.all()
    return render(request, 'departments.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname, "departments": departments})

# #Controlador de Celdas
# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='logout')
def celdas(request):
    title = "Celdas"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    celdas = Cells.objects.all()
    celdas_ccs = Cells.objects.filter(CellCity='CCS')
    celdas_gua = Cells.objects.filter(CellCity='GUA')
    celdas_hig = Cells.objects.filter(CellCity='HIG')
    celdas_cau = Cells.objects.filter(CellCity='CAU')
    print(celdas_ccs, celdas_gua, celdas_hig, celdas_cau)

    return render(request, 'celdas.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname, "celdas": celdas, "celdas_ccs": celdas_ccs,
                   "celdas_gua": celdas_gua, "celdas_hig": celdas_hig, "celdas_cau": celdas_cau})

# #Controlador de Actividades
# @user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='logout')
def activity(request):
    title = "Actividades"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    act = Activity.objects.all().order_by('-id')[:5]
    soportes = Activity.objects.filter(Act='SOPORTE')
    inst = Activity.objects.filter(Act='INSTALACION')
    celdafull = Activity.objects.filter(Act='CELDAFULL')
    celdamedia = Activity.objects.filter(Act='CELDAMEDIA')
    print(act)

    return render(request, 'activity.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname, "act": act, "soportes": soportes,
                   "inst": inst, "celdafull": celdafull, "celdamedia": celdamedia})

# #Controlador de statics
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='logout')
def charts(request):
    title = "POS Logs"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login

    return render(request, 'charts.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname})


# #Controlador de statics
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='logout')
def assignment(request):
    title = "Asignacion de Actividades"
    localtime = time.asctime(time.localtime(time.time()))
    username = request.user.username
    lastname = request.user.last_name
    firstname = request.user.first_name
    User = get_user_model()
    current_user = request.user
    usuario = User.objects.get(id=current_user.id)
    last_login = usuario.last_login
    form = AssignmentActivityForm(request.POST or None)

    return render(request, 'assignment.html',
                  {"title": title, "localtime": localtime, "last_login": last_login, "username": username,
                   "lastname": lastname, "firstname": firstname, "form": form})


# def error404(request, exception):
#     title = '404 Error'
#     return render(request, '404.html', {"title": title})

# Error 404
def handle_not_found(request, exection):
    title = '404 Error'
    return render(request, exection, '404.html', {"title": title})


@login_required(login_url='logout')
def logout_view(request):
    title = "Logout"
    localtime = time.asctime(time.localtime(time.time()))
    logout(request)
    return redirect('/login/', {"title": title, "localtime": localtime})
