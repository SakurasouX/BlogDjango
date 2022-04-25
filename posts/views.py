from django.shortcuts import render

from .models import Post


def index(request):
    pd = Post.objects.all()
    context = {'posts': pd}
    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    context = {'post_id': post_id}
    return render(request, 'posts/post_detail.html', context)
