from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})
