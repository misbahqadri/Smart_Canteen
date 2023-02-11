from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('main/',views.main1, name='main1'),
    path('reslogin/', views.reslogin, name='reslogin'),
    path('signup/', views.handleSignUp, name='handleSignUp'),
    path('register/', views.register_form, name='register_form'),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('checkout/', views.checkout, name="Checkout"),
    path('productView/<int:myid>', views.productView, name="productView"),
    path('orderView/', views.orderView, name="orderView"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="shop/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="shop/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="shop/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="shop/password_reset_done.html"),
         name="password_reset_complete"),

]