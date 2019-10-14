from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.Signup, name="Signup"),
    path('login/', views.loginView, name="login"),
    path('profile/', views.profile),
    path('logout/', LogoutView.as_view(), name='logout')


]
