from django.urls import path
# from .views import home, about, cse_student,Student_Add,student_detail,student_update,student_delete
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('about-us', about, name='aboutus'),
    path('cse-student', cse_student, name='cse'),
    path('add-form', Student_Add, name='add-form'),
    path('student-detail/<pk>',student_detail,name='student-detail'),
    path('student-update/<pk>',student_update, name='student-update'),
    path('student-delete/<pk>',student_delete, name='student-delete'),

    # CBV
    path('teacher-profile',TeacherProfileView.as_view(), name='teacher-profile'),
    path('teacher-profile/details/<int:pk>/', TeacherProfileDetailView.as_view(), name='teacher-detail'),
    path('teacher-profile/add',TeacherProfileCreateView.as_view(), name='teacher-add'),
    path('teacher-profile/update/<int:pk>',TeacherProfileUpdateView.as_view(),name='teacher-update'),
    path('teacher-profile/delete/<int:pk>',TeacherProfileDeleteView.as_view(),name='teacher-delete'),
]
