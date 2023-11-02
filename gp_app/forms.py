from django.forms import ModelForm
from .models import Business #, Project

"""
#create class for project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =('title', 'description')
"""
class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'is_open','email', 'address', 'city', 'phone_number', 'about')
