from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView, DeleteView,CreateView
from .models import Blog
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/blog_update.html"
    fields = ["title","body"]
    success_url = reverse_lazy("blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_delete.html"
    success_url = reverse_lazy("blog_list")


class BlogCreateView(CreateView):
    model = Blog
    template_name = "blog/blog_create.html"
    fields = "__all__"
    success_url = reverse_lazy("blog_list")
