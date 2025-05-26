from django.db import models

from users.models import CustomUser


# Create your models here.

class Files(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()
    files = models.ManyToManyField(Files)


class Enrollment(models.Model):
    state_choices = (
        ('applied', 'Applied'),
        ('enrolled', 'Enrolled'),
        ('rejected', 'Rejected'),
    )
    state = models.CharField(max_length=100, choices=state_choices, default='applied')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)