from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


def form_text(request):
    return render(request, 'posts/text_render.html')
