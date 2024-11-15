from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import *
from .serializers import UserRegisterSerializer, CourseSerializer, StudentSerializer

#register user
class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            # copy of data saved in student table
            userdata ={
                "username": request.data.get('name'),
                "email": request.data.get('email'),
                "password": request.data.get('password')     
            }
            Userializer = UserRegisterSerializer(data=userdata)
            if Userializer.is_valid():
                Userializer.save()
                get_user = User.objects.get(username=request.data.get('name'))
                request.data['user'] = get_user.id
                student = StudentSerializer(data=request.data)
                if student.is_valid():
                    student.save()
                    return Response({
                        'status': 2,
                        'message': 'User Registered Successfully'
                        })
                return Response(student.errors, status=400)
            return Response(Userializer.errors, status=400)
        return Response(serializer.errors, status=400)
        
#course
class CourseView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 2,
                'message': 'Course Created Successfully'})
        return Response(serializer.errors, status=400)


#student
class StudentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
         user_id = request.user.id
         student = Student.objects.get(user=user_id)
         serializer = StudentSerializer(student)
         return Response(serializer.data)

    # def post(self, request):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': 'Student Created Successfully'})
    #     return Response(serializer.errors, status=400)
    def put (self, request):
        # Update Student
        id = request.data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 2,'message': 'Student Updated Successfully'})
        return Response(serializer.errors, status=400)

class CourseAddView(APIView):
    permission_classes = [IsAuthenticated]
    def post (self, request):
        # Update Student course ids
        user_id = request.user.id
        student = Student.objects.get(user=user_id)
        # update student course ids
        student.course_ids = request.data.get('course_ids')
        student.save()
        return Response({'status': 2,'message': 'Course Added Successfully'})




        