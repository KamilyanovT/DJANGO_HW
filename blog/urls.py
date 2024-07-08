from django.contrib import admin
from django.urls import path
from .views import blog_catalog, post_detail

urlpatterns = [
    path('', blog_catalog, name='blog_catalog'),
    path('<slug:slug>/', post_detail, name='post_detail'),

]
