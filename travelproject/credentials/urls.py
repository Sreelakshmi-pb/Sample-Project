from .import views
from django.urls import path
app_name = 'credentials'
urlpatterns = [


    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.custom_login, name='login'),



]