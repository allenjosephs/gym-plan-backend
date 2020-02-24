# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import *
from rest_framework import permissions, generics
from rest_framework.decorators import *

from .serializers import *
from .models import Equipment

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def welcome(request):
    """ Welcome message to indicate server is up and running """
    return Response({"message": "gym plan backend up and running!"})

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_current_user(request):
    """ Retrieve logged-in user data """
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)

class CreateUserView(APIView):
    """ Create new user """
    permission_classes = (permissions.AllowAny, )

    def post(self,request):
        user = request.data.get('user')
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})

        serializer = UserSerializerWithToken(data = user)

        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})

        return Response({"response" : "success", "message" : "user created succesfully"})

class EquipmentList(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class MuscleGroupList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

class ExerciseList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutList(generics.ListAPIView):
    """
    View to retrieve all workouts in the system
    Only available to site admins.
    """
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class UserWorkoutList(generics.ListAPIView):

    serializer_class = WorkoutSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Workout.objects.filter(creator=user_id)

class WorkoutCreate(generics.CreateAPIView):
    serializer_class = WorkoutSerializerCreate

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class SetCreate(generics.CreateAPIView):
    serializer_class = SetSerializerCreate