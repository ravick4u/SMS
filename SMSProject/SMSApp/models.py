from django.apps import apps
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    interest = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='student_pictures/')
    resume = models.FileField(upload_to='student_resumes/')
    certificates = models.FileField(upload_to='student_certificates/')
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students_created')
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students_modified')

    class Meta:
        app_label = 'SMSApp'
        #app_label = apps.get_containing_app_config('SMSApp').name