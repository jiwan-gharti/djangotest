from django.views.generic import ListView, DeleteView
from .models import Post


class PostListView(ListView):
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')


class PostDetailView(DeleteView):
    model = Post
    template_name = 'post_detail.html'
