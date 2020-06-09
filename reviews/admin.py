from django.contrib import admin
from .models import Author, language, Project

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('language',)


# Register your models here.
admin.site.register(Author)
admin.site.register(language)
admin.site.register(Project, ProjectAdmin)