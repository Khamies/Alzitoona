from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from Alzitoona.settings import MEDIA_ROOT


class Student(models.Model):

    user=models.OneToOneField(User,unique=True)
    nickname=models.CharField(max_length=100,default="user")
    index = models.CharField("index", max_length=20, unique=True)
    specialization = models.CharField("specialization", max_length=100)
    phone_number = models.CharField("Phone Number", max_length=10)
    age = models.CharField("age",max_length=5)
    related_interest = models.CharField("Related Interest",max_length=20)
    photo_name=models.CharField("photo name",max_length=100,default="")
    photo=models.FileField(upload_to=MEDIA_ROOT,default=None)





    def __unicode__(self):
        return self.user.username




class Professor(models.Model):

    user=models.OneToOneField(User,unique=True)
    professor_id=models.AutoField(primary_key=True,unique=True,default=None)
    nickname=models.CharField("nick name",max_length=100,default="user")
    specialization = models.CharField("specialization", max_length=100)
    phone_number = models.CharField("Phone Number", max_length=10)
    photo_name=models.CharField("photo name",max_length=100,default="")
    photo=models.FileField(upload_to=MEDIA_ROOT,default=None)
    upvote=models.IntegerField("up vote",default=0)
    downvote=models.IntegerField("down vote",default=0)
    total_votes=models.IntegerField("total votes",default=0)



    def __unicode__(self):
        return self.user.username

