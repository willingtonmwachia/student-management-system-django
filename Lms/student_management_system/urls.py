from django.urls import path
from .views import (
    signup,
    user_login,
    admin_dashboard,
    add_student,
    add_teacher,
    add_parent,
    add_course,
    add_assignment,
    add_unit,
    add_exam  # Add this line
)

urlpatterns = [
    path('', admin_dashboard, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add_student/', add_student, name='add_student'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('add_parent/', add_parent, name='add_parent'),
    path('add_course/', add_course, name='add_course'),
    path('add_assignment/', add_assignment, name='add_assignment'),
    path('add_unit/', add_unit, name='add_unit'),
    path('add_exam/', add_exam, name='add_exam'),  # Add this line
]
from django.urls import path
from .views import (
    student_list, add_student,
    parent_list, add_parent,
    teacher_list, add_teacher,
    course_list, add_course,
)

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/add/', add_student, name='add_student'),
    
    path('parents/', parent_list, name='parent_list'),
    path('parents/add/', add_parent, name='add_parent'),
    
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/add/', add_teacher, name='add_teacher'),
    
    path('courses/', course_list, name='course_list'),
    path('courses/add/', add_course, name='add_course'),
]
