from __future__ import unicode_literals

from django.db import models

from Begining.models import Professor


class Professor_Rating(models.Model):
    professor=models.ForeignKey(Professor)
    comment=models.CharField("comment",max_length=300)

    def __unicode__(self):
        return self.comment