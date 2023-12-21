from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import PostBlog


# Create your views here.
class BlogListView(ListView):
    model = PostBlog
    template_name = "blogs.html"


class BlogDetailView(DetailView):
    model = PostBlog
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = PostBlog
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = PostBlog
    template_name = "post_update.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = PostBlog
    template_name = "post_delete.html"
    success_url = reverse_lazy("blogs")
