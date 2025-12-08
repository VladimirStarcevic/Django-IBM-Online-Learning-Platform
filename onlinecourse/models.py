from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User # Uvozimo standardni Django User Model
from django.utils.timezone import now

class Course(models.Model):
    name = models.CharField(max_length=100, default="online course")
    description = models.CharField(max_length=500)
    pub_date = models.DateField(default=now) # Publicaton date
    # M:M veza sa Instructor se obično dodaje ovde, ali za sada Lab to ne traži

    def __str__(self):
        return self.name

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 1:1 veza ka Django Useru
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=0)

    def __str__(self):
        return f"Instructor: {self.user.first_name} {self.user.last_name}"