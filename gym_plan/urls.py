from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('exercises/', views.ExerciseList.as_view(), name='exercise_list'),
    path('workouts/', views.WorkoutList.as_view(), name='workout_list'),
    path('workouts/userWorkouts/', views.UserWorkoutList.as_view(), name='user_workout_list'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workout_create'),
    path('workouts/update/<int:pk>', views.WorkoutDetail.as_view(), name='workout_update'),
    path('workouts/delete/<int:pk>', views.WorkoutDetail.as_view(), name='workout_delete'),
    path('sets/create/', views.SetCreate.as_view(), name='set_create'),
    path('muscle_groups/', views.MuscleGroupList.as_view(), name='muscle_group_list'),
    path('users/create/', views.CreateUserView.as_view(), name='create_user'),
    path('users/currentUser/', views.get_current_user),
]