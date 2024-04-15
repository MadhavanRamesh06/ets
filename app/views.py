from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import AssignmentForm ,CourseForm
from .models import Course, Grade, Assignment

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')
    
@login_required
def rdirect(req):
    return render(req,'index.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    courses = Course.objects.filter(user=user)
    grades = Grade.objects.filter(course__user=user)
    assignments = Assignment.objects.filter(course__user=user)
    return render(request, 'home.html', {'user': user, 'courses': courses ,'grade':grades , 'assignments':assignments})

@login_required
def course_detail(request,course_id):
    user = request.user
    courses = Course.objects.filter(user=user)
    course = Course.objects.get(id=course_id)
    grades = Grade.objects.filter(course__user=user)
    assignments = Assignment.objects.filter(course=course_id)
    return render(request, 'course_detail.html', {'course': course,'courses': courses, 'grade':grades, 'assignments':assignments })

def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form})
    
def delete_course(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('dashboard')
    
@login_required
def grade_tracking(request):
    user = request.user
    course = Course.objects.filter(user=user)
    grades = Grade.objects.filter(course__user=user)
    return render(request, 'grade_tracking.html', {'grades': grades, 'courses':course})

@login_required
def assignment_management(request):
    user = request.user
    course = Course.objects.filter(user=user)
    assignments = Assignment.objects.filter(course__user=user)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = user
            assignment.save()
            return redirect('assignment_management')
    else:
        form = AssignmentForm()
    return render(request, 'assignment_management.html', {'assignments': assignments, 'courses':course, 'form': form})

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    assignment.delete()
    return redirect('assignment_management')

def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_management')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'edit_assignment.html', {'form': form})

@login_required
def add_assignment(request):
    if request.method == 'POST':
        # If form is submitted
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_management')
    else:
        form = AssignmentForm()

@login_required
def add_course(request):
    if request.method == 'POST':
        form =CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_management')
    else:
        form = CourseForm()

@login_required
def course_management(request):
    user = request.user
    courses = Course.objects.filter(user=user)
    return render(request,'course_management.html',{'courses':courses})
