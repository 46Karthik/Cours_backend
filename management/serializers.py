from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'name', 'description', 'price', 'image')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'user', 'name', 'email', 'phone', 'gender', 'file', 'course_ids')
        