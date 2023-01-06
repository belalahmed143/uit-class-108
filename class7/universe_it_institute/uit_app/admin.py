from django.contrib import admin
from .models import Student,Department,ContactUs,TeacherProfile
# Register your models here.

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(ContactUs)
admin.site.register(TeacherProfile)
