from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    path('list_test/', views.list_test, name="list_test"),
    path('home/', views.home, name="home"),
]
