from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('handlesignup/', views.handlesignup, name='handlesignup'),
    path('signup/', views.signup, name='signup'),
    path('handlelogin/', views.handlelogin, name='handlelogin')
]