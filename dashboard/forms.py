from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','interested']


class EmailUpdateForm(forms.Form):
    old_email = forms.EmailField(label='Current email', required=True)
    new_email = forms.EmailField(label='New email address', required=True)
    password_email = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)


