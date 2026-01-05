from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.PostListViews.as_view(), name="posts"),
    path('posts/<pk>/',views.PostDetailViews.as_view(), name="post_detail"),
    path('add/', views.addPost, name="add_post"),

]