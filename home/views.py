from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post, Category
from .models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .forms import Contact


# Create your views here.


def home(request):

    Posts = Post.objects.all().order_by('-postTimeDate')
    paginator = Paginator(Posts, 5)
    page = request.GET.get('page')

    #?page = 2

    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]

    Posts = paginator.get_page(page)

    context = {'Posts': Posts,
               'Categories': Category.objects.all()[0:4],
               'RecentPost': Recent}
    return render(request, 'home/home.html', context)


def readMore(request, slug):
    # return HttpResponse(f'this is blogPost : {slug}')

    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]
    post = Post.objects.filter(postId=slug).first()
    context = {'post': post,
             'Categories': Category.objects.all()[0:4],
             'RecentPost': Recent}

    return render(request, 'home/readMore.html', context)


def search(request):
    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]
    query = request.GET['search']
    allPosts = Post.objects.filter(Q(postTitle__icontains=query) | Q(postText__contains=query))
    parms = {'allPosts': allPosts,
             'Categories': Category.objects.all(),
             'RecentPost': Recent}
    return render(request, 'home/search.html', parms)

def contact(request):
    context = {'RecentPost': Post.objects.all()[0:4],
            'Categories': Category.objects.all()[0:4]}
    if request.method == 'POST':
        name = request.POST['uname']
        email = request.POST['email']
        text = request.POST['text']

        if len(name) < 2 or len(email) < 3:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(Name=name, Email=email, Content=text)
            contact.save()
            messages.success(request, "your comment added successfully")
    return render(request, 'home/contact.html',context)


def aboutMe(request):
    return render(request, 'home/aboutMe.html')

def contactUs(request):
    context = {}
    if request.POST:
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['Contact'] = form
    else:  # GET request
        form = Contact()
        context = {'form': form}
    return render(request, 'home/contact.html', context)

