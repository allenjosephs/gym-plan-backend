from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.db import models
from django.contrib.auth.models import User
from .models import Equipment, MuscleGroup, Exercise, Workout, Set, ExerciseSet, SetWorkout

class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'date_joined')

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
        fields = ('token', 'id', 'username', 'password', 'first_name',
        'last_name', 'email', 'is_staff', 'is_superuser', 'date_joined')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'date_joined')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'img_url', 'icon_url',)

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ('id', 'name', 'img_url', 'icon_url',)

class ExerciseSerializer(serializers.ModelSerializer):
    primary_equip = EquipmentSerializer(many=False, read_only=True)
    primary_muscle = MuscleGroupSerializer(many=False, read_only=True)
    secondary_musclegroup = MuscleGroupSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'primary_equip', 'primary_muscle', 'secondary_musclegroup', 'instructions', )

class ExerciseSetSerializer(serializers.ModelSerializer):
    exercise_name = serializers.SerializerMethodField()
    primary_equip = serializers.SerializerMethodField()

    def get_exercise_name(self, obj):
        return obj.exercise.name

    def get_primary_equip(self, obj):
        return obj.exercise.primary_equip.icon_url

    class Meta:
        model = ExerciseSet
        fields = ('order', 'exercise_name', 'primary_equip')

class SetSerializer(serializers.ModelSerializer):
    exercises = ExerciseSetSerializer(source='set_exercises', many=True, read_only=True)

    class Meta:
        model = Set
        fields = ('label', 'set_repeat_count', 'interval_duration_secs', 'interval_rest_between', 'interval_rest_duration', 'exercises')

class SetWorkoutSerializer(serializers.ModelSerializer):

    aSet = SetSerializer(many=False, read_only=True)

    class Meta:
        model = SetWorkout
        fields = ('order', 'aSet', )

class WorkoutSerializer(serializers.ModelSerializer):

    creator_id = serializers.SerializerMethodField()
    creator_username = serializers.SerializerMethodField()
    creator_name = serializers.SerializerMethodField()

    sets = SetWorkoutSerializer(source='setworkout_set', many=True, read_only=True)

    def get_creator_id(self, obj):
        return obj.creator.id

    def get_creator_username(self, obj):
        return obj.creator.username

    def get_creator_name(self, obj):
        name = f'{obj.creator.first_name} {obj.creator.last_name}' if obj.creator.first_name else ''
        return name

    class Meta:
        model = Workout
        fields = ('id', 'name', 'description', 'creator_id', 'creator_username', 'creator_name', 'users', 'sets', 'workout_warmup', 'workout_warmup_duration', 'workout_cooldown', 'workout_cooldown_duration', 'set_rest_between', 'set_rest_duration')


class WorkoutSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('id', 'name', 'description', 'workout_warmup', 'workout_warmup_duration', 'workout_cooldown', 'workout_cooldown_duration', 'set_rest_between', 'set_rest_duration', 'creator')


