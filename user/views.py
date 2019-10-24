from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from posts.models import post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def registerPage(request):
    rf=forms.register_form(request.POST or None)
    if rf.is_valid():
        user=User.objects.create_user(rf.cleaned_data['username'],rf.cleaned_data['email'],rf.cleaned_data['password'])
        user.first_name=rf.cleaned_data['first_name']
        user.last_name=rf.cleaned_data['last_name']
        user.save()
        return HttpResponseRedirect('/')

    return render(request,'user/register.html',{'rf':rf})


def loginPage(request):
    lf=forms.login_form(request.POST or None)
    if lf.is_valid():
        u=lf.cleaned_data['username']
        p=lf.cleaned_data['password']
        r=authenticate(username=u,password=p)
        if r is not None:
            login(request,r)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Enter Valid Username')

    return render(request,'user/login.html',{'lf':lf})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request,id):
    user=User.objects.get(id=id)
    u_posts=post.objects.filter(user=user)
    context={
        'u_posts':u_posts,
        'user':user,
    }
    return render(request,'user/profile.html',context)