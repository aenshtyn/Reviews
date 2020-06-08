from django.shortcuts import render, redirect
from django.http  import HttpResponse,  Http404
import datetime as dt
from .models import Project

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.all_projects()
    return render(request, 'reviews/index.html', {"date" : date, "projects": projects })