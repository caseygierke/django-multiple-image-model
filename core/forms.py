from .models import Project
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'event_date', 'registration_deadline', 'pictures')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                