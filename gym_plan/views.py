from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from .serializers import *

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def auth_check(request):
    """Simple view to test token authentication"""
    content = {'message': 'Your authentication has been confirmed!'}
    return Response(content)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_current_user(request):
    """Retrieve logged-in user data"""
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)

# View to create a new user
class CreateUserView(APIView):
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