from .models import Project
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title',  'gugun', 'type', 'gender', 'cost', 'period', 'deadline', 'content', 'start_at')