from django import forms
from django.contrib.auth.models import User


class userlogin(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password']

from django.contrib.auth.forms import UserCreationForm



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user