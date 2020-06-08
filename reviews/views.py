from django.shortcuts import render, redirect
from django.http  import HttpResponse,  Http404
import datetime as dt
from .models import Project

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.all_projects()
    return render(request, 'reviews/index.html', {"date" : date, "projects": projects })

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'reviews/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'reviews/search.html',{"message":message})