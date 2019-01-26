from __future__ import unicode_literals

from django.db import models

from Alzitoona.settings import MEDIA_ROOT


class ask_question(models.Model):
    asker=models.CharField("Asker",max_length=100,default="User")
    question_id=models.AutoField(unique=True,primary_key=True,default=None)
    question_title = models.CharField("question title", max_length=150, default=None)
    question = models.CharField("question", max_length=1000, default=None)
    specialization = models.CharField("specialization", max_length=50, default=None)
    date = models.DateField("date", auto_now_add=True)
    upvote=models.IntegerField("upvote",default=0)
    downvote=models.IntegerField("downvote",default=0)
    all_votings=models.IntegerField("Voters",default=0)
    weekday= models.IntegerField("week day",default=0)
    dayOfWeek=models.IntegerField("day Of Week",default=1)


    def __unicode__(self):
        return unicode(self.question_title)



class answer(models.Model):
    answer_id=models.AutoField(primary_key=True,unique=True,default=None)
    asker = models.CharField("asker", max_length=30, default=None)
    answer_by=models.CharField("answer by",max_length=100,default="User")
    question_key = models.ForeignKey(ask_question)
    answer = models.CharField("answer", max_length=800, default=None)
    up_vote = models.IntegerField("upvote",  default=0)
    down_vote = models.IntegerField("downvote",  default=0)
    all_votings=models.IntegerField("voters",default=0)
    weekday= models.IntegerField("week day",default=1)
    dayOfWeek=models.IntegerField("day Of Week",default=1)
    comment = models.CharField("comment", max_length=200, default="no comment")

    def __unicode__(self):
        return self.answer


class libarary(models.Model):

    uploader=models.CharField("Upload by",max_length=100,default="User")
    file_name=models.CharField("File Name",max_length=200,default="File")
    file_id=models.AutoField(primary_key=True,unique=True,default=None)
    file = models.FileField("file", upload_to=MEDIA_ROOT, default=None, null=True, blank=True)
    specialization = models.CharField("specialization", max_length=50, default="general")
    description=models.CharField("description",max_length=200,default="no description")
    date = models.DateTimeField("date", auto_now_add=True)
    weekday= models.IntegerField("week day",default=0)
    dayOfWeek=models.IntegerField("day Of Week",default=1)


    def __unicode__(self):
        return self.file.path

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.file.storage, self.file.path
        # Delete the model before the file
        super(libarary, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)
