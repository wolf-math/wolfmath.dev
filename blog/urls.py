from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog'),
]
