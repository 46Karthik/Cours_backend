from django.db import models
from django.contrib.auth.models import User

 
# create a model  student 
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    course_ids = models.CharField(max_length=100)

# create a model  course
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=200)

