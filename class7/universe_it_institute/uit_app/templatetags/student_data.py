from django import template
from uit_app.models import Student

register = template.Library()

@register.filter()
def all_student(request):
    students = Student.objects.filter()
    return students

@register.filter()
def cse_student(request):
    students = Student.objects.filter(department__department_name='CSE')
    return students

@register.filter()
def eee_student(request):
    students = Student.objects.filter(department__department_name='EEE')
    return students