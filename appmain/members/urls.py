from django.contrib import admin
from django.urls import path,include
#from userapp import views as main_views
from . import views
urlpatterns = [
    path("register/", views.RegisterApi.as_view()),
    path('login/', views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view()),
    path("wlcmmail/",views.send_welcome_email),
]