from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post, Category
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


def home(request):

    Posts = Post.objects.all().order_by('-postTimeDate')
    paginator = Paginator(Posts, 5)
    page = request.GET.get('page')

    #?page = 2

    Recent = Post.objects.all().order_by('-postTimeDate')[0:5]

    Posts = paginator.get_page(page)

    context = {'Posts': Posts,
               'Categories': Category.objects.all(),
               'RecentPost': Recent}
    return render(request, 'home/home.html', context)


def readMore(request, slug):
    # return HttpResponse(f'this is blogPost : {slug}')

    Recent = Post.objects.all().order_by('-postTimeDate')[0:5]
    post = Post.objects.filter(postId=slug).first()
    context = {'post': post,
             'Categories': Category.objects.all(),
             'RecentPost': Recent}

    return render(request, 'home/readMore.html', context)


def search(request):
    Recent = Post.objects.all().order_by('-postTimeDate')[0:5]
    query = request.GET['search']
    allPosts = Post.objects.filter(Q(postTitle__icontains=query) | Q(postText__contains=query))
    parms = {'allPosts': allPosts,
             'Categories': Category.objects.all(),
             'RecentPost': Recent}
    return render(request, 'home/search.html', parms)