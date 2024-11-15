from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('course/', CourseView.as_view(), name='course'),
    path('course/<int:id>/', StudentView.as_view(), name='student'),
    path('student/', StudentView.as_view(), name='student'),

   path('courseAdd/', CourseAddView.as_view(), name='courseAdd'),
    
]