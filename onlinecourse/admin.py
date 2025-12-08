from django.contrib import admin
from .models import Course, Instructor # Uvezi modele

# Register your models here.

# Uvezi i User, iako ga ne registrujemo direktno

# Registracija modela - ovo stvara tabelu u Admin Panelu
admin.site.register(Course)
admin.site.register(Instructor)
