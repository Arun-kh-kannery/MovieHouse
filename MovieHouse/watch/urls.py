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
from django.urls import path
from watch import views
app_name="watch"
urlpatterns = [
    path('add_to_watchlist/<int:pk>',views.add_to_watchlist,name="add_to_watchlist"),
    path('view_watchlist',views.viewwatchlist,name="watchlist_view"),
    path('add_watchlist/<int:pk>',views.add_to_Swatchlist,name="swatchlist"),
    path('Mwatchlist/', views.viewMwatchlist, name="Mwatchlist"),
    path('remove/<int:pk>',views.mremove,name="mremove"),
    path('sremove/<int:pk>', views.sremove, name="sremove"),
    path('subscribe/',views.subscribe,name="subscribe"),
    path('freetrial/',views.freetrial,name="freetrial"),
    path('subscription/',views.subscription,name="subscription"),
    path('annual/', views.subscription2, name="subscription2")

]
