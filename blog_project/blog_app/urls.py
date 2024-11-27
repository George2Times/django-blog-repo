from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='blog_app/login.html',
        extra_context={'next': '/dashboard/'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog_app/logout.html'), name='logout'),
    # path('', home_view, name='home'),
    path('', views.post_list, name='post-list'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:post_id>/edit/', views.post_update, name='post-update'),
]

