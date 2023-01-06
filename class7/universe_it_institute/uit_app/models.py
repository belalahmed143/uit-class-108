from django.db import models
from django.urls import reverse
# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=200)
    s_session  = models.CharField(max_length=20, default='2022-2026')

    def __str__(self):
        return self.department_name

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='StudentImage')
    roll = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return self.student_name

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email
    
class TeacherProfile(models.Model):
    name = models.CharField(max_length=200)
    designation  = models.CharField(max_length=50)
    image = models.ImageField(upload_to='TeacherProfile')


    def __str__(self):
        return self.name


