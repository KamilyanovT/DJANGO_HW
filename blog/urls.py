from django.contrib import admin
from django.urls import path
from .views import blog_catalog, post_detail, category_detail, tag_detail

urlpatterns = [
    path('', blog_catalog, name='blog_catalog'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('tag/<slug:slug>/', tag_detail, name='tag_detail'),

]
