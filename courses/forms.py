from django import forms
from .models import courseName


class createcourse(forms.ModelForm):
    class Meta:
        model = courseName
        fields = ('name', 'image')
