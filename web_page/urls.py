from django.urls import path
from . import views

urlpatterns = [
    path('', views.web_page, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
