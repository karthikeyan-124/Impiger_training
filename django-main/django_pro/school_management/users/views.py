from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, StudentProfileSerializer,StudentGradeSerializer
from .models import StudentProfile
from .permissions import IsAdmin, IsTeacher
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


User = get_user_model()

# ✅ User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# ✅ User Login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ List all users (Admin only)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

# ✅ Student views their grade
class StudentGradeView(generics.RetrieveAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.student_profile

# ✅ Admin creates teachers
class CreateTeacherView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAdmin]

    def perform_create(self, serializer):
        serializer.save(role="teacher")

# ✅ Teacher creates a student
class CreateStudentView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsTeacher]

    def perform_create(self, serializer):
        serializer.save(role="student")


import logging
from django.http import Http404

logger = logging.getLogger('myapp')  # Use the custom logger from settings.py

class AddGradeView(generics.UpdateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeacher]

    def get_queryset(self):
        return StudentProfile.objects.all()

    def get_object(self):
        student_id = self.kwargs.get('student_id')
        logger.debug(f"Received student_id: {student_id}")  # Log the student_id

        try:
            student = StudentProfile.objects.get(user__id=student_id)
            logger.debug(f"Student found: {student}")
            return student
        except StudentProfile.DoesNotExist:
            logger.error(f"Student with ID {student_id} not found")
            raise Http404("Student not found")

# ✅ Admin Deletes User
class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_object(self):
        user_id = self.kwargs.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            if user.role == "admin":
                raise serializers.ValidationError("Cannot delete Admin user")
            return user
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

