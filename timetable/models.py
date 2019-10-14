from django.db import models
from courses.models import courseName
from django.contrib.auth.models import Permission, User

# Create your models here.


class timetable(models.Model):
    coursename = models.ForeignKey(courseName, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    duration = models.IntegerField()
