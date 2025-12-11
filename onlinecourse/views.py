from django.shortcuts import render
from .models import Course
# onlinecourse/views.py


# onlinecourse/views.py

def course_list(request):
    course_list_qs = Course.objects.order_by('-total_enrollment')[:10]

    context = {
        'course_list': course_list_qs, # key 'course_list'
    }
    return render(request, 'onlinecourse/course_list.html', context)

