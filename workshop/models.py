from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Workshop(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    overview = models.TextField()
    course_details = models.TextField()
    project = models.TextField()
    level = models.CharField(blank=True, max_length=100)
    number_of_seats = models.IntegerField()
    poster = models.ImageField(upload_to='workshop/poster/', null=True, blank=True)
    start_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(Workshop)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    roll_number = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.batch
