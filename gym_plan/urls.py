from django.urls import path, include
from django.contrib import admin
# from rest_framework_simplejwt.views import obtain_jwt_token
# from .views import home
from . import views

urlpatterns = [
    path('users/create/', views.CreateUserView.as_view(), name='create_user'),
    path('users/getUsrDtls/', views.get_current_user, name='get_user_details'),
    path('users/authCheck/', views.auth_check, name='auth_check'),
]