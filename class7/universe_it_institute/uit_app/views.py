from django.shortcuts import render,redirect
from .models import Student
from .forms import *

# Create your views here.

def home(request):
    v_students = Student.objects.all().order_by('?')[:10]
    cse_students = Student.objects.filter(department__department_name='CSE')

    c_form = ContactForm(request.POST)
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('home')
    context = {
        'v_students':v_students,
        'cse_students':cse_students,
        'c_form':c_form
    }
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def cse_student(request):
    return render(request, 'cse.html')

def Student_Add(request):
    students = Student.objects.all().order_by('?')[:10]
    form = StudentAddForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = StudentAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-form')
    return render(request, 'student-add.html', {'form':form,'students':students})


def student_detail(request,pk):
    student = Student.objects.get(pk=pk)
    context ={
        'student':student
    }
    return render(request, 'student-detail.html', context)

def student_update(request,pk):
    student = Student.objects.get(pk=pk)
    form = StudentAddForm(request.POST, request.FILES,)
    if request.method == 'POST':
        form = StudentAddForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentAddForm(instance=student)
    context ={
        'student':student,
        'form':form
    }
    return render(request, 'student-update.html', context)

def student_delete(request,pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('/')
    return render(request, 'student-delete.html')



from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class TeacherProfileView(ListView):
    model = TeacherProfile
    template_name ='teacher-profile.html'
    context_object_name ='teachers'

class TeacherProfileDetailView(DetailView):
    model = TeacherProfile
    template_name ='teacher-detail.html'

class TeacherProfileCreateView(CreateView):
    model = TeacherProfile
    fields =['image','name','designation']
    template_name = 'teacher-add.html'
    success_url = reverse_lazy('teacher-profile')

class TeacherProfileUpdateView(UpdateView):
    model = TeacherProfile
    fields =['image','name','designation']
    template_name = 'teacher-add.html'
    success_url = reverse_lazy('teacher-profile')

class TeacherProfileDeleteView(DeleteView):
    model = TeacherProfile
    template_name = 'teacher-delete.html'
    success_url = reverse_lazy('teacher-profile')