from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout #
from .models import Course
# onlinecourse/views.py


# onlinecourse/views.py

def course_list(request):
    course_list_qs = Course.objects.order_by('-total_enrollment')[:10]

    context = {
        'course_list': course_list_qs, # key 'course_list'
    }
    return render(request, 'onlinecourse/course_list.html', context)

def enroll(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()

        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

    # Ako neko slučajno ode na ovu adresu sa GET, moramo vratiti nešto!
    return HttpResponseRedirect(reverse(viewname='onlinecourse:course_list')) # Vrati ga na listu kurseva

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course
    }
    return render(request, 'onlinecourse/course_detail.html', context)

def login_view(request):
    # OVDE BI IŠAO KOD ZA GET I POST LOGIKU
    # Za sada samo vraćamo praznu stranicu
    return render(request, 'onlinecourse/login.html', {})

# NOVO: LOGOUT VIEW (koristi ugrađenu Django funkciju)
def logout_view(request):
    logout(request) # <--- Koristi ugrađenu funkciju
    return redirect('onlinecourse:course_list') # Preusmeri nazad na Home


