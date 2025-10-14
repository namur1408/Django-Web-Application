from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from members_app.models import Member
from django.core.exceptions import ObjectDoesNotExist

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def enroll_course(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        member = Member.objects.get(user=request.user)
    except ObjectDoesNotExist:
        member = Member.objects.create(user=request.user)
    course.members.add(member)
    return redirect('course_list')


