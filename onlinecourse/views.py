from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout #
from .models import Course



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
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onlinecourse:course_list')
        else:
            message = 'Invalid credentials. Please try again.'
    return render(request, 'onlinecourse/login.html', {'message': message})

def user_registration(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        if user is not None:
          login(request, user)
          return redirect('onlinecourse:course_list')
        else:
          message = 'Username already registered.'
    return render(request, 'onlinecourse/login.html', {'message': message})


def user_registration(request):
    message = ''
    if request.method == 'POST':
        # 1. DOHVATANJE SVIH POLJA IZ FORME (Name atributi)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password'] # psw se menja u password
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        # 2. PROVERA: Da li username već postoji?
        if User.objects.filter(username=username).exists():
            message = 'Username already registered.'
        else:
            # 3. KREIRANJE NOVOG USERA (sa firstname/lastname)
            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=firstname, last_name=lastname) # Dodeljujemo first/last name

            if user is not None:
                # 4. Automatski Login i Redirect
                login(request, user)
                return redirect('onlinecourse:course_list')
            else:
                message = 'Registration failed. Please check your data.' # Neuspešna kreacija

    # GET Request ili neuspeli POST vraćaju formu
    return render(request, 'onlinecourse/signup.html', {'message': message}) # Novo: Rendujemo signup.html

# NOVO: LOGOUT VIEW (koristi ugrađenu Django funkciju)
def logout_view(request):
    logout(request) # <--- Koristi ugrađenu funkciju
    return redirect('onlinecourse:course_list') # Preusmeri nazad na Home


