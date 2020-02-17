# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
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

class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer