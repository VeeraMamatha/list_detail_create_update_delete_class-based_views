from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *

class school_list(ListView):
    model=school
    context_object_name='schools'
    ordering=['sname']
    #queryset=School.objects.filter(id=1)
    #template_name='app/school_list.html'
