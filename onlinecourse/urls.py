# onlinecourse/urls.py
from django.urls import path
from . import views # Uvozimo view funkcije iz istog foldera

urlpatterns = [
    # NOVO: Root putanja ('') u ovom ruteru se poklapa sa /onlinecourse/
    # Poziva se funkcija views.index
    path('list/', views.course_list, name='course_list'),
]