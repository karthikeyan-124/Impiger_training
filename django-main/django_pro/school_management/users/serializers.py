from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, StudentProfile

# User Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.role == 'student':
            StudentProfile.objects.create(user=user)  # Create StudentProfile automatically
        return user

# User Login Serializer with JWT Token
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "role": user.role,
        }

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']

# Student Profile Serializer (For Viewing Grades)
class StudentProfileSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(source='student.username', read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['student_username', 'grade']


# Student Profile Serializer (Update Grade)
class StudentGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['grade']
        extra_kwargs = {'grade': {'required': True}}

    def update(self, instance, validated_data):
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance

