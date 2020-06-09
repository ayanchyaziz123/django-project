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


# Create your views here.

def teacherHome(request):
    form = PostForm()
    return render(request, 'teachers/teachersHome.html', {'title': 'add-newpost', 'form': form})


def studentList(request):
    StudentList = Student.objects.all()
    context = {'StudentList': StudentList}
    return render(request, 'teachers/studentList.html', context)


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



