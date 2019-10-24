from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from . import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

def home(request):
    posts=models.post.objects.all()
    return render(request,'posts/index.html',{'posts':posts})


def add_post(request,user_id):
    f=forms.addPost_form(request.POST or None)
    if f.is_valid():
        post=models.post()
        user1=User.objects.get(id=user_id)
        post.user=user1
        post.title=f.cleaned_data['title']
        post.content=f.cleaned_data['content']
        post.date=datetime.now()
        post.save()
        return HttpResponseRedirect('/')

    return render(request,'posts/addpost.html',{'f':f})

def post_detail(request,id):
    posts=models.post.objects.get(id=id)
    return render(request,'posts/postdetail.html',{'posts':posts})

def post_edit(request,id,user_id):
    post=models.post.objects.get(id=id)
    uf=forms.editpost_form(request.POST or None,instance=post)
    if uf.is_valid():
        post.title=uf.cleaned_data['title']
        post.content=uf.cleaned_data['content']
        post.date=datetime.now()
        post.save()
        return redirect('profile',id=user_id)

    return render(request,'posts/postedit.html',{'uf':uf})