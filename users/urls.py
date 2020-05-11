from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login, name='login'),
    path("signup_company", views.signup_company, name='signup_company'),
    path("signup_user", views.signup_user, name='signup_user'),
    path("logout", views.logout, name='logout'),
]