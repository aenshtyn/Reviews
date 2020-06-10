from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Project, ProjectUpdateRecipients
from .forms import ProjectUpdatesForm, NewProjectForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.all_projects()

    if request.method == 'POST':
        form = ProjectUpdatesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = ProjectUpdateRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('index')
    else:
        form = ProjectUpdatesForm()
    return render(request, 'reviews/index.html', {"date" : date, "projects": projects, "letterForm":form })

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'reviews/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'reviews/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()



    return render(request,"reviews/project.html", {"project":project})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'reviews/new_project.html', {"form": form})


def projectupdate(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = ProjectUpdateRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)