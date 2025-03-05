from django.urls import path
from .swagger import schema_view
from .views import (
    RegisterView, LoginView, UserListView, StudentGradeView, 
    CreateTeacherView, CreateStudentView,AddGradeView,DeleteUserView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('students/grade/', StudentGradeView.as_view(), name='student-grade'),
    path('teachers/create/', CreateTeacherView.as_view(), name='create-teacher'),
    path('students/create/', CreateStudentView.as_view(), name='create-student'),
    path('teachers/add-grade/<int:student_id>/', AddGradeView.as_view(), name='add-grade'),
    path('admin/delete-user/<int:user_id>/', DeleteUserView.as_view(), name='delete-user'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
    ]


