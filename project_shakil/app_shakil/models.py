from django.db import models
import datetime
import os


def filepath(request, filename):
    old_file = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" %(timenow, old_file)
    return os.path.join('uploads/', filename)

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    dob = models.DateTimeField('Date of Birth')
    user_email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

class Blog(models.Model):
    blog_image = models.ImageField(upload_to=filepath, null=True, blank=True)
    blog_title = models.CharField(max_length=200)
    blog_body = models.CharField(max_length=2000)
    blog_dateTime = models.DateTimeField(null=True)
    blog_type = models.CharField(max_length=100, null=True)
    
class Work(models.Model):
    work_image=models.ImageField(upload_to=filepath, null=True, blank=True )
    work_title=models.CharField(max_length=200)
    work_tools=models.CharField(max_length=200)
    work_url=models.CharField(max_length=200)