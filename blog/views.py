from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post

# Create your views here.
class BlogHomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 20


class BlogPostView(DetailView):
    model = Post
    context_object_name = 'post'

