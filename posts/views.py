from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})


@login_required()
def create(request):
    """Creation of a new article by a registered user"""
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.pub_date = timezone.now()
        post.user = request.user
        post.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'posts/create.html')


def update(request, pk):
    """Article update by registered user"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.update_time = timezone.now()
        post.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'posts/update.html', {'post': post})


def delete(request, pk):
    """Delete article"""
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect('/')
