from django.urls import path
from . import views

urlpatterns = [
    path('authChecker/', views.AuthChecker.as_view(), name='auth_checker'),
]