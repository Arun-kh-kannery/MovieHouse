"""
URL configuration for MovieHouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from movie import views
app_name="movie"
urlpatterns = [
    path('',views.base,name="base"),
    path('login/',views.user_login,name="login"),
    path('register/',views.user_register,name="register"),
    path('movie_home/',views.movie_home,name="home"),
    path('details/<m>',views.movie_details,name="details"),
    path('language/<l>',views.movie_language,name="language"),
    path('watch/<int:m>',views.movie_watch,name="watchmovie"),
    path('logout/',views.user_logout,name="logout"),
    path('home/',views.home_all,name="homeall"),
]
