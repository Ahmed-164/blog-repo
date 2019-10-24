from django import forms
from posts.models import post

class addPost_form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = post
        fields = ('title', 'content')
class editpost_form(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=post
        fields=('title','content')