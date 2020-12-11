from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid


# Create your models here.
class Enterprise(models.Model):
    name = models.CharField(max_length=20)

class Task(models.Model):
    name = models.CharField(max_length=20)

class Resume(models.Model):
    name = models.CharField(max_length=10)
    motivation = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resume')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="resume")

def resume_image_path(instance,filename):
    uuidstr = str(uuid.uuid1())
    total = uuidstr+filename
    return 'api/resume/{0}'.format(total)

class ResumeImage(models.Model):
    image = models.ImageField(upload_to=resume_image_path)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,related_name='resumeimage')