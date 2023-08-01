from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('log',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
