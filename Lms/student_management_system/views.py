from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Replace with your desired redirect
    else:
        form = SignUpForm()
    return render(request, 'student_management_system/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace with your desired redirect
    else:
        form = LoginForm()
    return render(request, 'student_management_system/login.html', {'form': form})
from django.shortcuts import render

def home(request):
    return render(request, 'student_management_system/home.html')  # Create this template later

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'student_management_system/dashboard.html')






@login_required
def add_student(request):
    # Logic to add a student goes here
    return render(request, 'student_management_system/add_student.html')

@login_required
def add_teacher(request):
    # Logic to add a teacher goes here
    return render(request, 'student_management_system/add_teacher.html')

@login_required
def add_parent(request):
    # Logic to add a parent goes here
    return render(request, 'student_management_system/add_parent.html')

@login_required
def add_course(request):
    # Logic to add a course goes here
    return render(request, 'student_management_system/add_course.html')

@login_required
def add_unit(request):
    # Logic to add a unit goes here
    return render(request, 'student_management_system/add_unit.html')

@login_required
def add_exam(request):
    # Logic to add an exam goes here
    return render(request, 'student_management_system/add_exam.html')

@login_required
def add_assignment(request):
    # Logic to add an assignment goes here
    return render(request, 'student_management_system/add_assignment.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_student(request):
    if request.method == "POST":
        # Handle form submission for adding a student
        # Save student logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_student.html')

@login_required
def add_teacher(request):
    if request.method == "POST":
        # Handle form submission for adding a teacher
        # Save teacher logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_teacher.html')

@login_required
def add_parent(request):
    if request.method == "POST":
        # Handle form submission for adding a parent
        # Save parent logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_parent.html')

@login_required
def add_course(request):
    if request.method == "POST":
        # Handle form submission for adding a course
        # Save course logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_course.html')

@login_required
def add_assignment(request):
    if request.method == "POST":
        # Handle form submission for adding an assignment
        # Save assignment logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_assignment.html')
@login_required
def add_unit(request):
    if request.method == "POST":
        # Handle form submission for adding a unit
        # Save unit logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_unit.html')
@login_required
def add_unit(request):
    if request.method == "POST":
        # Handle form submission for adding a unit
        # Save unit logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_unit.html')
@login_required
def add_unit(request):
    if request.method == "POST":
        # Handle form submission for adding a unit
        # Save unit logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_unit.html')
@login_required
def add_unit(request):
    if request.method == "POST":
        # Handle form submission for adding a unit
        # Save unit logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_unit.html')
@login_required
def add_exam(request):
    if request.method == "POST":
        # Handle form submission for adding an exam
        # Save exam logic here
        return redirect('admin_dashboard')  # Redirect to the dashboard after adding
    return render(request, 'student_management_system/add_exam.html')








from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Parent, Teacher, Course
from .forms import StudentForm, ParentForm, TeacherForm, CourseForm

# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_management_system/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_management_system/add_student.html', {'form': form})

# Parent Views
def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'student_management_system/parent_list.html', {'parents': parents})

def add_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_list')
    else:
        form = ParentForm()
    return render(request, 'student_management_system/add_parent.html', {'form': form})

# Teacher Views
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'student_management_system/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'student_management_system/add_teacher.html', {'form': form})

# Course Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'student_management_system/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'student_management_system/add_course.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from .models import Course, Teacher

def add_course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        teacher = Teacher.objects.get(id=teacher_id)
        Course.objects.create(name=name, teacher=teacher)
        return redirect('course_list')  # Redirect to the course list after adding

    teachers = Teacher.objects.all()  # Get all teachers
    return render(request, 'student_management_system/add_course.html', {'teachers': teachers})
