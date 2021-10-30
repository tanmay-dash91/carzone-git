from django.db import models

# Create your models here.

class Team(models.Model):


    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    photos = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    fblink = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname