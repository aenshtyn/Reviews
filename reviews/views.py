from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Project, ProjectUpdateRecipients
from .forms import ProjectUpdatesForm, NewProjectForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


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


class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)


    def get_parser_context (self, request, format=None):
        all_projs = Project.objects.all()
        serializers = ProjectSerializer(all_projs, many = True )
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        permission_classes = (IsAdminOrReadOnly,)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)