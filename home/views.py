from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post, Category


# Create your views here.


def home(request):
    Posts = Category.objects.all()
    context = {'Posts': Posts}
    return render(request, 'home/home.html', context)