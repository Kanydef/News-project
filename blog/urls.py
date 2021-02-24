from django.urls import path
from .views import BlogListView, BlogDetailView, BlogUpdateView,BlogDeleteView,BlogCreateView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("update/<int:pk>", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="blog_delete"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),

]
