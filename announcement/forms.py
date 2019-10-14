from django import forms
from .models import Announcement, comment


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "content", "image",]


class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ["text", ]
