from django.db import models

# Create your models here.

from django.db import models

class Details(models.Model):
    Name = models.CharField(max_length=500)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    w_mobile = models.CharField(max_length=50)
    stage = models.CharField(max_length=100)
    occupation = models.CharField(max_length=200)
    skills = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(null=True,blank=True)
    #created_date = models.DateTimeField("date published")
    #def __str__(self):
    #    return self.Name