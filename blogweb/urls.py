from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('posts/delete-all/', views.delete_all_my_posts, name='delete_my_posts'),

    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='blogweb/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),
]