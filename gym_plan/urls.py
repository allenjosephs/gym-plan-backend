from django.urls import path, include
from . import views

urlpatterns = [
    path('users/create/', views.CreateUserView.as_view(), name='create_user'),
    path('users/currentUser/', views.get_current_user),
]