from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Issue(models.Model):
    type = models.CharField(
        max_length=100,
        choices=[('Hardware', 'Hardware'), ('Software', 'Software')]
    )
    room = models.CharField(max_length=100)
    urgent = models.BooleanField(default=False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='issues', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type} Issue in {self.room}'

    def get_absolute_url(self):
        return reverse('itreporting:issue-detail', kwargs={'pk': self.pk})


class Module(models.Model):
    name = models.CharField(max_length=100)  # Name of the module
    description = models.TextField()  # Description of the module
    date_added = models.DateTimeField(default=timezone.now)  # Date when the module is added
    instructor = models.ForeignKey(User, related_name='modules', on_delete=models.CASCADE)  # Instructor who teaches the module

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('itreporting:module-detail', kwargs={'pk': self.pk})


class Course(models.Model):
    name = models.CharField(max_length=100)
    module = models.ForeignKey(Module, related_name='courses', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.module.name})"


class Registration(models.Model):
    student = models.ForeignKey(User, related_name='registrations', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='registrations', on_delete=models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} registered for {self.course.name}"


