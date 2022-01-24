from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=25)
    secondname = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    Primaryscool = models.CharField(max_length=200)
    highschool = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    position = models.CharField(max_length=25, default="Member")
    email = models.EmailField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profilepics', default='default.jpg')
    DateJoined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('member_detail', kwargs={'pk': self.pk})


class Project(models.Model):
    projectId = models.CharField(primary_key=True, max_length=10)
    projectname = models.CharField(max_length=200)
    projectdescription = models.TextField()
    project_pic = models.ImageField(null=True, blank=True, upload_to='projectpics', default='default.jpg')
    projectmanager = models.ForeignKey(member, on_delete=models.CASCADE)

    def __str__(self):
        return self.projectname

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})


class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    time_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f'{self.author}'
