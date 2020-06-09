from django import forms
from .models import Project

class ProjectUpdatesForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['author', 'pub_date']
        widgets = {
            'language': forms.CheckboxSelectMultiple(),
        }