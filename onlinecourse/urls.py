# onlinecourse/urls.py
from django.urls import path
from . import views # Uvozimo view funkcije iz istog foldera
app_name = 'onlinecourse'

urlpatterns = [
    # NOVO: Root putanja ('') u ovom ruteru se poklapa sa /onlinecourse/
    # Poziva se funkcija views.index
    path('list/', views.course_list, name='course_list'),
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
