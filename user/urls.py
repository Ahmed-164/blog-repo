from django.urls import path
from . import views

urlpatterns=[
path('register/',views.registerPage,name='register'),
path('login/',views.loginPage,name='login'),
path('logout/',views.log_out,name='logout'),
path('profile/<int:id>',views.profile,name='profile'),

]