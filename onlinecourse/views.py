from django.shortcuts import render
from .models import Course
# onlinecourse/views.py


def course_list(request):

    all_courses = Course.objects.all()
    context = {
        'all_courses': all_courses,
    }
    return render(request, 'onlinecourse/course_list.html', context)
