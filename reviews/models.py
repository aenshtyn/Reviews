from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.name} Profile'
    
    class Meta:
        ordering = ['name']


class language(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Project (models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField ()
    author = models.ForeignKey(User,on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to = 'projects/', blank=True)
    link = models.URLField(blank=True)
    post = models.TextField(blank=True)

    def __str__(self):
        return self.name


    
    @classmethod
    def all_projects(cls):
        today = dt.date.today()
        projects = cls.objects.filter(pub_date__date = today)
        return projects

    @classmethod
    def search_by_name(cls,search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects

    class Meta:
        ordering = ['name']

    def save_project(self):
        self.save()


class ProjectUpdateRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.project} Rating'



