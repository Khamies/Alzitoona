from django import forms
from django.forms import FileField

from Questions.models import libarary


class myLibrary (forms.ModelForm):

   class Meta:
       model=libarary
       fields=['file','specialization']

