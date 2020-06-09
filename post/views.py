from django.shortcuts import render
from .models import Post


# Create your views here.

def postHome(request):
    Posts = Post.objects.all()
    context = {'Posts': Posts}
    return render(request, 'post/post.html', context)


def viewPost(request, slug):
    # return HttpResponse(f'this is blogPost : {slug}')

    post = Post.objects.filter(postId=slug).first()
    context = {'post': post}

    return render(request, 'post/viewPost.html', context)
