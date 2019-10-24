from django import forms
from django.contrib.auth.models import User
class register_form(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')


class login_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)