from django.http import HttpRequest
from django.shortcuts import render, redirect
from post.models import Category, Post, PostForm
from home.models import Student
import csv
from django.http import HttpResponse
from django.contrib import messages
import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import  AccountAuthenticationForm
from user.models import Account
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def teacherHome(request):
    context = {}
    if request.user.is_authenticated:
       form = PostForm()
       return render(request, 'teachers/teachersHome.html', {'title': 'add-newpost', 'form': form})

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'teachers/logIn.html', context)


def log(request):
    return render(request, 'teachers/logIn.html')

def studentList(request):
    context = {}
    if request.user.is_authenticated:
        StudentList = Student.objects.all()
        context = {'StudentList': StudentList}
        return render(request, 'teachers/studentList.html', context)

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'teachers/logIn.html', context)

def teachersLogIn(request):
    return render(request, 'teachers/studentList.html')


# to add teachers post

def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        messages.success(request, "your Post added successfully")
        return redirect('teacherHome')


# to export student deatils

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="cse44th c&d .xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('cse-44th-C+D')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Name', 'Email', 'Phone', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Student.objects.all().values_list('studentId', 'name', 'email', 'phone')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

# to export student attendance



def login_view(request):

     context = {}

     user = request.user
     if user.is_authenticated and user.is_admin==True:
        return redirect("home")

     if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user and user.is_admin==True:
                login(request, user)
                return redirect("teacherHome")

     else:
        form = AccountAuthenticationForm()

     context['login_form'] = form
     return render(request, 'teachers/logIn.html', context)