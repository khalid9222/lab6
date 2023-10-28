from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students = Student.objects.all()
    form = StudentForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('students')
    
    return render(request, 'students.html', {'students': students, 'form': form})

def courses(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('courses')
    
    return render(request, 'courses.html', {'courses': courses, 'form': form})

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    courses = student.courses.all()
    form = CourseForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            course_id = form.cleaned_data['course']
            course = Course.objects.get(pk=course_id)
            student.courses.add(course)
    
    available_courses = Course.objects.exclude(students=student)
    
    return render(request, 'details.html', {'student': student, 'courses': courses, 'form': form, 'available_courses': available_courses})

