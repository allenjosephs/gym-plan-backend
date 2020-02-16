from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User

class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'date_joined')

class UserSerializerWithToken(serializers.ModelSerializer):

    # password is set to write_only to prevent it from being returned in the response
    password = serializers.CharField(write_only=True)

    # token is our JWT token
    # note: SerializerMethodField() takes a method name and with zero args will default
    # to get_<field_name>.  In this case, "get_token", which is defined below.
    token = serializers.SerializerMethodField()

    def get_token(self, object):
        """Function to return a properly encoded JWT"""

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)

        return token

    def create(self, validated_data):
        """Purpose: Create a new user"""
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name',
        'last_name', 'email', 'is_staff', 'is_superuser', 'date_joined')