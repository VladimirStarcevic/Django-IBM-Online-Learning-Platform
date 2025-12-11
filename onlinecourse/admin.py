# onlinecourse/admin.py

from django.contrib import admin
# Uvozimo sve modele
from .models import Course, Instructor, Lesson, Question, Choice, Enrollment, Submission, Learner
# Uvozimo User za referencu u Adminu, ako nam zatreba
from django.contrib.auth.models import User


# --- INLINE KLASE (Pomoćni Šalteri) ---

# 1. Lesson Inline: Pomoćni šalter za Lekcije
class LessonInline(admin.StackedInline):
    model = Lesson # <--- Model koji se spaja
    extra = 5      # <--- Koliko praznih polja da se prikaže

# 2. Question Inline: Pomoćni šalter za Pitanja
class QuestionInline(admin.StackedInline):
    model = Question # <--- Model koji se spaja
    extra = 5


# --- MODEL ADMIN KLASE (Glavni Šalteri) ---

# Pravila za prikaz Kursa
class CourseAdmin(admin.ModelAdmin):
    # Polja koja će biti prikazana u glavnoj formi za unos (SQL SELECT)
    fields = ['name', 'description', 'pub_date', 'image']

    # KLJUČNA LINIJA: Vizuelno spajanje relacija N:1 na JEDNU stranicu!
    inlines = [LessonInline, QuestionInline]

    # Dodatno: Polja koja ce se prikazati na LISTI svih kurseva
    list_display = ('name', 'pub_date')


# Pravila za prikaz Instruktora
class InstructorAdmin(admin.ModelAdmin):
    # user polje se bira iz postojece Django User tabele
    fields = ['user', 'full_time', 'total_learners']

    # Dodatno: Prikaz na listi
    list_display = ('user', 'full_time', 'total_learners')


# --- REGISTRACIJA (Aktivacija) ---

# Registracija sa Custom Pravilima
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)

# Registracija ostalih modela (bez posebnih pravila za sada)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Submission)
admin.site.register(Learner)