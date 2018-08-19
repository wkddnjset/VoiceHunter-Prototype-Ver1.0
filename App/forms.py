from .models import Project, Gugun
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title',  'gugun', 'type', 'gender', 'cost', 'period', 'deadline', 'content', 'start_at')
    GUGUN_CHOICES = list()
    guguns = Gugun.objects.all()
    for gugun in guguns:
        GUGUN_CHOICES.append((str(gugun.id), str(gugun.gugun)))

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={
            'class': 'form-control form-control-sm mb-1',
            'name': 'title',
            'autocomplete': 'off',
            'required':'requireds'})
        self.fields['gugun'].widget = forms.Select(
            attrs={
            'class': 'form-control form-control-sm mb-1',
            'name': 'gugun'},
            choices=self.GUGUN_CHOICES
        )
        self.fields['type'].widget = forms.Select(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'type'},
            choices=Project.TYPE_CHOICES
        )
        self.fields['gender'].widget = forms.Select(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'gender'},
            choices=Project.GENDER_CHOICES
        )
        self.fields['cost'].widget = forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'cost',
                'autocomplete': 'off',
                'placeholder':'예) 100000'},
        )
        self.fields['period'].widget = forms.NumberInput(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'period',
                'autocomplete': 'off',
                'placeholder': '예) 15'},
        )
        self.fields['deadline'].widget = forms.TextInput(
            attrs={
                'id': 'deadline_datepicker',
                'class': 'form-control form-control-sm mb-1',
                'name': 'deadline',
                'autocomplete': 'off'},
        )
        self.fields['content'].widget = forms.Textarea(
            attrs={
                'class': 'form-control form-control-sm mb-1',
                'name': 'content',
                'autocomplete': 'off'},
        )
        self.fields['start_at'].widget = forms.TextInput(
            attrs={
                'id': 'start_datepicker',
                'class': 'form-control form-control-sm mb-1',
                'name': 'start_at',
                'autocomplete': 'off'},
        )