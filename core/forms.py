from .models import Image, Project
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'event_date', 
            'registration_deadline',
        ]
