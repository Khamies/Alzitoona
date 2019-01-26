from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import View


class chat(View):
    def get(self,request):
        return render_to_response("ask.html")